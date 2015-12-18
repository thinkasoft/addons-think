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


class report_hr_payslip_extended(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(report_hr_payslip_extended, self).__init__(
            cr, uid, name, context
        )

        self.localcontext.update({
            'get_payslip_lines': self._get_payslip_lines,
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
        return super(report_hr_payslip_extended, self).set_context(
            objects,
            data,
            ids,
            report_type=report_type
        )

    def _get_payslip_lines(self, obj):
        res = []
        dic = {}
        self.cr.execute(
            "SELECT he.identification_id, he.name_related, SUM(pl.amount), "
            "ROUND(SUM(pl.amount)/100, 2), ROUND((SUM(pl.amount)*2)/100, 2), "
            "ROUND(ROUND(SUM(pl.amount)/100, 2) + ROUND((SUM(pl.amount)*2)/100, 2), 2) "
            "FROM hr_payslip_line AS pl,hr_payslip AS hp,hr_employee AS he "
            "WHERE pl.code = '039' "
            "AND pl.slip_id = hp.id "
            "AND pl.employee_id = he.id "
            "AND hp.date_to >= %s AND hp.date_to <= %s "
            "AND ( hp.state = 'done' OR hp.state = 'paid' )"
            "GROUP by he.identification_id, he.name_related,pl.code "
            "ORDER by he.identification_id", (self.date_from, self.date_to))

        for x in self.cr.fetchall():
            dic = {
                'payslip_employeeid': x[0],
                'payslip_namerelated': x[1],
                'amount': x[2],
                'rpvh': x[3],
                'faov': x[4],
                'mount': x[5]
            }
            res.append(dic)
        return res

report_sxw.report_sxw(
    'report.hr.payslip.extended.mako',
    'hr.payslip.extended',
    'addons-think/hr_payslip_extended/report/report_hr_payslip_extended_webkit.mako',
    parser=report_hr_payslip_extended
)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
