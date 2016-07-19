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

    def _get_total_deductions(self, cr, uid, ids, field_names, arg=None,
                              context=None):
        """
            Calculates the accumulated annually of the employee, this reset
            each Year
            @param ids: id the employee selected.
            @return: Dictionary with the sum fo the salary the employee yearly.
        """
        res = dict()
        payslip_line_obj = self.pool.get('hr.payslip.line')
        payslip_obj = self.pool.get('hr.payslip')
        employee_obj = self.pool.get('hr.employee')
        today = datetime.datetime.now()
        suma = 0.0

        # Iterates by each month of the Year
        for month in xrange(1, 13):

            # Takes the the first and lastest day of the month
            datemonthstart = "%s-%s-01" % (today.year, month)
            datemonthend = "%s-%s-%s" % (today.year, month,
                                         calendar.monthrange(today.year,
                                                             month)[1])

            # Converts of String to Datetime
            datemonthstart = datetime.datetime.strptime(datemonthstart,
                                                        "%Y-%m-%d")
            datemonthend = datetime.datetime.strptime(datemonthend, "%Y-%m-%d")

            # Defined query sql
            condition_slip = [('date_to', '>=', datemonthstart),
                              ('date_to', '<=', datemonthend),
                              ('employee_id', 'in', ids),
                              '|', ('state', '=', 'done'),
                              ('state', '=', 'paid')]

            # Execute query, gets one list of ids (hr.payslip)
            slip_ids = payslip_obj.search(cr, uid, condition_slip)

            # Defined query sql 2
            condition_slip_line = [('slip_id', 'in', slip_ids),
                                   ('code', '=', '039')]

            # Execute query, gets one list of ids (hr.payslip.line)
            slip_line_ids = payslip_line_obj.search(cr, uid,
                                                    condition_slip_line)

            # Sum all slip_line founds and acumulate in "suma"
            for slip_browse in payslip_line_obj.browse(cr, uid, slip_line_ids,
                                                       context=None):
                suma += slip_browse.amount

            # Finds the employee for insert the total sum
            employee = employee_obj.browse(cr, uid, ids, context=None)
            res[employee[0].id] = suma

        return res

    def _calc_days(self, cr, uid, ids, field_names, arg=None, context=None):
        """
            Calcualted the number day holidays and holidays bonus of a employee
            (Only for venezuela)
            @param ids: id the employee selected.
            @return: Dictionary with the sum fo the salary the employee yearly.
        """
        res = dict()
        employee_obj = self.pool.get('hr.employee')

        # Gets date current
        today = datetime.datetime.now()

        # Searches for the employee object  that is related with ids
        for employee in employee_obj.browse(cr, uid, ids, context=None):
            # Gets admission date and converted of String to Datetime
            date_employee = datetime.datetime.strptime(employee.admission_date,
                                                       "%Y-%m-%d")
            result = 15 + today.year - date_employee.year - 1
            if result >= 15 and result <= 30:
                res[employee.id] = result
            elif result > 30:
                res[employee.id] = 30
            else:
                res[employee.id] = 15
        return res

    _columns = {
        'vat': fields.char(
            'Vat', size=12, required=True,
            help="Rif the employee"
        ),
        'withholding': fields.float('Income Withholding', size=5,
                                    digits=(2, 2), required=True,
                                    help="Retention rate ISRL"),
        'salary': fields.float(
            'Monthly salary',
            required=True,
            help="Monthly salary (for use of employment records only)"
        ),
        'admission_date': fields.date(
            'Date Admission',
            required=False,
            help="""Date Admission (for use of employment records and history
            of the worker only)""",
        ),
        'date_exit': fields.date(
            'Date Diacharge',
            required=False,
            help="""Date Diacharge(for use of employment records and history of
            the worker only)"""
        ),
        'employment_benefit': fields.boolean(
            'Employment Benefit?',
            help="""Monthly salary is integral(for use of employment records
            and history of the worker only)"""
        ),
        'reference_bank': fields.char('Reference Bank', size=50),
        'number_days_benefits': fields.integer(
            'Number days benefits', size=3,
            help="""Only for venezuelathe la LOTTTS(ley organica del Trabajo de
            los trabajadores y trabajadoras Sociales) indica que debe comenzar
            en 60"""
        ),
        'other_benefits_deductions': fields.float(
            'Other benefits deductions',
            size=7, digits=(5, 2),
            help="""during the liquidation of earnings, benefits or settlement
            if any additional expense for discounting is placed in this field
            (request of client)"""
        ),
        'number_day_holidays': fields.function(
            _calc_days,
            type='integer',
            string='Number day holidays',
            help="""Starts in 15 days continuous and increment 1 days for each
            year"""
        ),
        'holidays_bonus': fields.function(
            _calc_days, type='integer',
            string='Holidays bonus',
            help="""Starts in 15 days continuous and increment 1 days for each
            year""",
        ),
        'december_salary_aprox': fields.float('December salary aprox',),
        'salary_yearly': fields.function(
            _get_total_deductions, type='float',
            string='Salary annually of employee'
        ),
        'acum_social_benefits': fields.float(
            'Acum social benefits',
            help="If employee brings accumulated social benefit in his history"
         ),
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
