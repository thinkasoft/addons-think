# !/usr/bin/python
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
##############################################################################
#    Copyright (C) 2015 thinkasoft , C.A. (www.thinkasoft.com)
#    All Rights Reserved
# ############## Credits ######################################################
#    Developed by: thinkasoft , C.A.
#    Coded by: Aular Hector Manuel (aular.hector3@gmail.com)
##############################################################################

import datetime
import calendar
from openerp.osv import osv, fields


class Payroll_extension(osv.Model):
    """Inherited res.partner"""

    _inherit = 'hr.employee'

    def _get_total_deductions(self, cr, uid, ids, field_names, arg=None, context=None):
        res = dict()
        payslip_line_obj = self.pool.get('hr.payslip.line')
        payslip_obj = self.pool.get('hr.payslip')
        employee_obj = self.pool.get('hr.employee')
        today = datetime.datetime.now()
        suma = 0.0

        for month in xrange(1, 13):
            datemonthstart = "%s-%s-01" % (today.year, month)
            datemonthend = "%s-%s-%s" % (today.year, month, calendar.monthrange(today.year, month)[1])

            datemonthstart = datetime.datetime.strptime(datemonthstart, "%Y-%m-%d")
            datemonthend = datetime.datetime.strptime(datemonthend, "%Y-%m-%d")

            condition_slip = [('date_to', '>=', datemonthstart),
                              ('date_to', '<=', datemonthend),
                              ('employee_id', 'in', ids),
                              '|', ('state', '=', 'done'),
                              ('state', '=', 'paid')]

            slip_ids = payslip_obj.search(cr, uid, condition_slip)

            condition_slip_line = [('slip_id', 'in', slip_ids), ('code', '=', '039')]

            slip_line_ids = payslip_line_obj.search(cr, uid, condition_slip_line)

            for slip_browse in payslip_line_obj.browse(cr, uid, slip_line_ids, context=None):
                suma += slip_browse.amount

            employee = employee_obj.browse(cr, uid, ids, context=None)
            res[employee[0].id] = suma

        return res

    def _calc_days(self, cr, uid, ids, field_names, arg=None, context=None):
        res = dict()
        today = datetime.datetime.now()
        employee_obj = self.pool.get('hr.employee')

        for employee in employee_obj.browse(cr, uid, ids, context=None):
            date_employee = datetime.datetime.strptime(employee.admission_date, "%Y-%m-%d")
            result = 15 + today.year - date_employee.year - 1
            if result >= 15 and result <= 30:
                res[employee.id] = result
            elif result > 30:
                res[employee.id] = 30
            else:
                res[employee.id] = 15
        return res

    _columns = {
        'vat': fields.char('Vat', size=12, required=True),
        'withholding': fields.float('Income Withholding', size=5, digits=(2, 2), required=True),
        'salary': fields.float('Monthly salary', required=True),
        'admission_date': fields.date('Date Admission', required=False),
        'date_exit': fields.date('Date Diacharge', required=False),
        'employment_benefit': fields.boolean('Employment Benefit?'),
        'reference_bank': fields.char('Reference Bank', size=50),
        'number_days_benefits': fields.integer('Number days benefits', size= 3),
        'other_benefits_deductions': fields.float('Other benefits deductions', size=7, digits=(5, 2)),
        'number_day_holidays': fields.function(_calc_days, type='integer', string='Number day holidays'),
        'holidays_bonus': fields.function(_calc_days, type='integer', string='Holidays bonus'),
        'december_salary_aprox': fields.float('December salary aprox'),
        'salary_yearly': fields.function(_get_total_deductions, type='float', string='Salary yearly'),
        'acum_social_benefits': fields.float('Acum social benefits'),
    }

    _defaults = {
        'withholding': 0,
        'salary': 0,
        'vat': ' ',
        'other_benefits_deductions': 0,
        'number_days_benefits': 60,
        'december_salary_aprox': 0,
        'acum_social_benefits': 0.00,
    }
