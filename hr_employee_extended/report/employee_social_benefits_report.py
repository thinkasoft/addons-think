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


class EmployeeSocialBenefitsReport(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(EmployeeSocialBenefitsReport, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'get_payslip_total_lines': self._get_payslip_total_lines,
        })

    def _get_payslip_total_lines(self, employee_obj):
        res = []
        dic = {}
        days_alic = 15
        hitoric_day = 5
        sum_days = 0
        payslip_line_obj = self.pool.get('hr.payslip.line')
        payslip_obj = self.pool.get('hr.payslip')
        date_init = datetime.datetime.strptime(employee_obj.admission_date, "%Y-%m-%d")
        today = datetime.datetime.now()

        aluc_month = ini_month = date_init.month
        final_month = 13
        sum_days = 2
        invalid_year = 2
        ini_year = date_init.year
        final_year = today.year

        while ini_year <= final_year:
            if ini_year == final_year:
                final_month = today.month + 1
            for month in xrange(ini_month, final_month):
                if aluc_month == month:
                    days_alic = days_alic + 1
                    if invalid_year is 0:
                        dic['hitoric_day'] = hitoric_day + sum_days
                        sum_days += 2
                    else:
                        invalid_year -= 1
                        dic['hitoric_day'] = 5
                else:
                    dic['hitoric_day'] = 5

                datemonthstart = "%s-%s-01" % (ini_year, month)
                datemonthend = "%s-%s-%s" % (ini_year, month, calendar.monthrange(ini_year, month)[1])
                datemonthstart = datetime.datetime.strptime(datemonthstart, "%Y-%m-%d")
                datemonthend = datetime.datetime.strptime(datemonthend, "%Y-%m-%d")

                condition_slip = [('date_to', '>=', datemonthstart),
                                  ('date_to', '<=', datemonthend),
                                  ('employee_id', '=', employee_obj.id),
                                  '|', ('state', '=', 'done'),
                                  ('state', '=', 'paid'),
                                  ]
                slip_ids = payslip_obj.search(self.cr, self.uid, condition_slip, context=False)
                condition_slip_line = [('slip_id', 'in', slip_ids),
                                       ('code', '=', '039')
                                       ]

                slip_line_ids = payslip_line_obj.search(self.cr, self.uid, condition_slip_line, context=False)
                dic = {'month': str(datemonthend.day) + "-" + str(datemonthend.month) + "-" + str(datemonthend.year),
                       'integral': 0}

                if slip_line_ids:
                    for slip_browse in payslip_line_obj.browse(self.cr, self.uid, slip_line_ids, context=None):
                        dic['integral'] += slip_browse.amount
                    dic['salary_daily'] = dic['integral'] / 30
                    dic['alic_benefit'] = ((dic['salary_daily'] * 60) / 12) / 30
                    dic['days_alic'] = days_alic
                    dic['holidays_bonus'] = ((dic['salary_daily'] * days_alic) / 12) / 30
                    dic['salary_integral'] = dic['salary_daily'] + dic['alic_benefit'] + dic['holidays_bonus']
                    res.append(dic)
            ini_month = 1
            ini_year += 1
        return res

report_sxw.report_sxw('report.employee.social.benefits.report',
                      'hr.employee',
                      'hr_employee_extended/report/employee_social_benefits_report.mako',
                      parser=EmployeeSocialBenefitsReport)
