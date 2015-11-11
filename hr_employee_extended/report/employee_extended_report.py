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


class EmployeeExtendedReport(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(EmployeeExtendedReport, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'otra_cosa': self.otra_cosa,
        })

    def otra_cosa(self, obj):
        res = []
        dic = {}
        list_month = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
        payslip_line_obj = self.pool.get('hr.payslip.line')
        payslip_obj = self.pool.get('hr.payslip')
        today = datetime.datetime.now()

        for month in xrange(1, 13):
            dateMonthStart = "%s-%s-01" % (today.year, month)
            dateMonthEnd = "%s-%s-%s" % (today.year, month, calendar.monthrange(today.year - 1, month)[1])

            dateMonthStart = datetime.datetime.strptime(dateMonthStart, "%Y-%m-%d")
            dateMonthEnd = datetime.datetime.strptime(dateMonthEnd, "%Y-%m-%d")

            slip_ids = payslip_obj.search(self.cr, self.uid,
                                          [('date_to', '>=', dateMonthStart), ('date_to', '<=', dateMonthEnd),
                                           ('employee_id', '=', obj.id)
                                           ],
                                          context=False)

            slip_line_ids = payslip_line_obj.search(self.cr, self.uid,
                                                    [('slip_id', '=', slip_ids),
                                                     '|', '|', '|', ('code', '=', '001'), ('code', '=', '003'), ('code', '=', '002'),
                                                     ('code', '=', '039')
                                                     ],
                                                    order='code', context=False)

            dic = {
                'month': list_month[month - 1],
                'basic': 0,
                'integral': 0,
            }

            for slip_browse in payslip_line_obj.browse(self.cr, self.uid, slip_line_ids, context=None):
                if slip_browse.code != '039':
                    dic['basic'] += slip_browse.amount
                else:
                    dic['integral'] += slip_browse.amount

            res.append(dic)
        return res
report_sxw.report_sxw('report.employee.extended.report',
                      'hr.employee',
                      'hr_employee_extended/report/employee_extended_report.mako',
                      parser=EmployeeExtendedReport)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
