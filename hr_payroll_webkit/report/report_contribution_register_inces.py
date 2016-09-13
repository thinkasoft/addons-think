# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
###########################################################################
#    Copyright (C) 2015 thinkasoft , C.A. (www.thinkasoft.com)
#    All Rights Reserved
# ############## Credits ######################################################
#    Developed by: thinkasoft , C.A.
#    Coded by:  Aular Hector Manuel (aular.hector3@gmail.com)
############################################################################

import time
from datetime import datetime
from dateutil import relativedelta

from openerp.report import report_sxw


class contribution_register_report_inces(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(contribution_register_report_inces, self).__init__(
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
        return super(contribution_register_report_inces, self).set_context(
            objects,
            data,
            ids,
            report_type=report_type
        )

    def _get_payslip_lines(self, obj):
        payslip_line = self.pool.get('hr.payslip.line')
        payslip_lines = list()
        res = list()
        dic = dict()
        ids_ant = 0
        self.cr.execute(
            "SELECT pl.id from "
            "hr_payslip_line as pl,"
            "hr_payslip AS hp,"
            "hr_employee AS he "
            "WHERE pl.slip_id = hp.id "
            "AND pl.employee_id = he.id "
            "AND (%s <= hp.date_to AND hp.date_to <= %s) "
            "AND pl.code = '039' "
            "AND ( hp.state = 'done' OR hp.state = 'paid')"
            "ORDER BY he.identification_id",
            (self.date_from, self.date_to))
        payslip_lines = [x[0] for x in self.cr.fetchall()]
        for line in payslip_line.browse(self.cr, self.uid, payslip_lines):
            if ids_ant == line.slip_id.employee_id.id:
                dic['amount'] += line.amount
                dic['rpvh'] = dic['amount'] / 100
                dic['faov'] = dic['amount'] * 2 / 100
                dic['mount'] = dic['rpvh'] + dic['faov']
            else:
                dic = dict(
                    payslip_name=line.slip_id.employee_id.name_related,
                    payslip_employeeid=line.slip_id.employee_id.
                    identification_id,
                    payslip_namerelated=line.slip_id.employee_id.name_related,
                    amount=line.total,
                    rpvh=float(line.amount) / 100,
                    faov=float(line.amount) * 2 / 100,
                    mount=(float(line.amount) / 100) + (float(line.amount) * 2)
                    / 100
                )
                ids_ant = line.employee_id.id
                res.append(dic)
        return res

report_sxw.report_sxw(
    'report.contribution.register.lines.webkit.inces',
    'hr.contribution.register',
    'addons/hr_payroll_webkit/report/'
    + 'report_contribution_register_webkit_inces.mako',
    parser=contribution_register_report_inces
)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
