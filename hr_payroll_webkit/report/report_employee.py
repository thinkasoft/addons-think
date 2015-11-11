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
            'get_payslip_lines': self._get_payslip_lines,
        })

    def _get_payslip_lines(self, obj):
        payslip_line = self.pool.get('hr.payslip.line')
        res = []
        ids = []
        for id in range(len(obj)):
            if obj[id].appears_on_payslip is True:
                ids.append(obj[id].id)
        if ids:
            res = payslip_line.browse(self.cr, self.uid, ids)
        return res

report_sxw.report_sxw('report.employee.report', 'hr.payslip',
 'hr_payroll_webkit/report/report_employee.mako', parser=employee_report, header=False)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
