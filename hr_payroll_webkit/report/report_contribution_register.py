# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011-2013 Serpent Consulting Services (<http://www.serpentcs.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
############################################################################
import time
from datetime import datetime
from dateutil import relativedelta

from openerp.report import report_sxw


class contribution_register_report(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(contribution_register_report, self).__init__(
            cr, uid, name, context
        )
        self.localcontext.update({
            'get_payslip_lines': self._get_payslip_lines,
            'sum_total': self.sum_total,
        })

    def set_context(self, objects, data, ids, report_type=None):
        self.date_from = data['form'].get(
            'date_from',
            time.strftime('%Y-%m-%d')
        )
        self.date_to = data['form'].get(
            'date_to',
            str(datetime.now() + relativedelta.relativedelta(
                months=+1,
                day=1,
                days=-1
            )
            )[:10]
        )
        return super(contribution_register_report, self).set_context(
            objects,
            data,
            ids,
            report_type=report_type
        )

    def sum_total(self):
        return self.regi_total

    def _get_payslip_lines(self, obj):
        payslip_line = self.pool.get('hr.payslip.line')
        payslip_lines = []
        res = []
        dic = {}
        ids_ant = 0
        self.regi_total = 0.0
        self.cr.execute("SELECT pl.id from hr_payslip_line as pl "
                        "LEFT JOIN hr_payslip AS hp on (pl.slip_id = hp.id) "
                        "WHERE (hp.date_from >= %s) AND (hp.date_to <= %s) "
                        "AND pl.register_id = %s "
                        "AND hp.state = 'done' "
                        "ORDER BY pl.employee_id",
                        (self.date_from, self.date_to, obj.id))
        payslip_lines = [x[0] for x in self.cr.fetchall()]
        for line in payslip_line.browse(self.cr, self.uid, payslip_lines):
            if ids_ant == line.slip_id.employee_id.id:
                dic['amount'] += line.amount
                if dic['amount'] != 0.0:
                    dic['rpvh'] = float(dic['amount']) / 100,
                    dic['faov'] = float(float(float(dic['amount']) * 2) / 100),
                    dic['mount'] = dic['rpvh'] + dic['faov']
                else:
                    dic['rpvh'] = 0.00
                    dic['faov'] = 0.00
                    dic['mount'] = 0.00
            else:
                dic = {
                    'payslip_name': line.slip_id.employee_id.name_related,
                    'payslip_employeeid':
                    line.slip_id.employee_id.identification_id,
                    'payslip_namerelated':
                    line.slip_id.employee_id.name_related,
                    'amount': line.amount,
                    'rpvh': float(line.amount) / 100,
                    'faov': float(line.amount * 2) / 100,
                    'mount': (float(line.amount) / 100) +
                    (float(line.amount) * 2) / 100
                }
                ids_ant = line.employee_id.id
                res.append(dic)
        return res

report_sxw.report_sxw(
    'report.contribution.register.lines.webkit',
    'hr.contribution.register',
    'addons/hr_payroll_webkit/report/report_contribution_register_webkit.mako',
    parser=contribution_register_report
)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
