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

import calendar
import datetime
from openerp.report import report_sxw


class EmployeeExtendedReportEmployee(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(EmployeeExtendedReportEmployee, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'get_payslip_lines': self._get_payslip_lines,
        })

    def _get_payslip_lines(self, obj):
        res = []
        dic = {}
        list_month_es = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo',
                         'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre',
                         'Noviembre', 'Diciembre']
        payslip_line_obj = self.pool.get('hr.payslip.line')
        payslip_obj = self.pool.get('hr.payslip')
        today = datetime.datetime.now()

        for month in xrange(1, 13):
            slip_ids = []
            slip_line_ids = []

            if month < 12:
                    datemonthstart = "%s-%s-01" % (today.year, month)
                    datemonthend = "%s-%s-%s" % (today.year, month, calendar.monthrange(today.year, month)[1])

                    datemonthstart = datetime.datetime.strptime(datemonthstart, "%Y-%m-%d")
                    datemonthend = datetime.datetime.strptime(datemonthend, "%Y-%m-%d")

                    condition_slip = [('date_to', '>=', datemonthstart), ('date_to', '<=', datemonthend),
                                      ('employee_id', '=', obj.id),
                                      '|', ('state', '=', 'done'), ('state', '=', 'paid'),
                                      ]
                    slip_ids = payslip_obj.search(self.cr, self.uid, condition_slip, context=False)

                    slip_line_ids = payslip_line_obj.search(self.cr, self.uid,
                                                            [('slip_id', 'in', slip_ids),
                                                             '|', '|', '|', '|', ('code', '=', '001'), ('code', '=', '003'),
                                                             ('code', '=', '002'), ('code', '=', '005'), ('code', '=', '039')
                                                             ],
                                                            order='code', context=False)

            dic = {
                'month': list_month_es[month - 1],
                'basic': 0,
                'integral': 0,
            }
            for slip_browse in payslip_line_obj.browse(self.cr, self.uid, slip_line_ids, context=None):
                if slip_browse.code != '039':
                    dic['basic'] += slip_browse.amount * slip_browse.quantity
                else:
                    dic['integral'] += slip_browse.amount

            res.append(dic)
        return res
report_sxw.report_sxw('report.employee.extended.report.employee',
                      'hr.employee',
                      'hr_employee_extended/report/employee_extended_report_employee.mako',
                      parser=EmployeeExtendedReportEmployee)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
