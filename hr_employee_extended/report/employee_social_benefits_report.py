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


class EmployeeSocialBenefitsReport(report_sxw.rml_parse):
    pass

report_sxw.report_sxw('report.employee.social.benefits.report',
                      'hr.employee',
                      'hr_employee_extended/report/employee_social_benefits_report.mako',
                      parser=EmployeeSocialBenefitsReport)
