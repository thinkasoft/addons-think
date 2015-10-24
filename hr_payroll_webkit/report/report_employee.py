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

from openerp.report import report_sxw


class employee_report(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(employee_report, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'otr_cosa': self.otra_cosa,
        })

    def otr_cosa(self):
        res = []
        print "Entro aqui"
        return res

report_sxw.report_sxw('report.employee', 'hr.payslip', 'hr_payroll_webkit/report/report_employee.mako', parser=employee_report)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
