#!/usr/bin/python
# -*- encoding: utf-8 -*-
###########################################################################
#    Copyright (C) 2015 thinkasoft , C.A. (www.thinkasoft.com)
#    All Rights Reserved
# ############## Credits ######################################################
#    Developed by: thinkasoft , C.A.
#
#    Coded by:  Aular Hector Manuel (aular.hector3@gmail.com)
#
##############################################################################
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

    def _get_payslip_lines(self, obj):
        payslip_line = self.pool.get('hr.payslip.line')
        payslip_lines = []
        res = []
        dic = {}
        ids_ant = 0
        self.cr.execute(
            "SELECT pl.id from "
            "hr_payslip_line as pl,"
            "hr_payslip AS hp,"
            "hr_employee AS he "
            "WHERE pl.slip_id = hp.id "
            "AND pl.employee_id = he.id "
            "AND (%s <= hp.date_to) AND (hp.date_to <= %s) "
            "AND pl.code = '039' "
            "AND hp.state = 'done' "
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
                dic = {
                    'payslip_name': line.slip_id.employee_id.name_related,
                    'payslip_employeeid':
                    line.slip_id.employee_id.identification_id,
                    'payslip_namerelated':
                    line.slip_id.employee_id.name_related,
                    'amount': line.total,
                    'rpvh': float(line.amount) / 100,
                    'faov': float(line.amount) * 2 / 100,
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
