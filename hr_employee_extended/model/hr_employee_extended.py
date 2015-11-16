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

import datetime
import calendar
from openerp.osv import osv, fields


class Payroll_extension(osv.Model):
    """Inherited res.partner"""

    _inherit = 'hr.employee'

    def _get_total_deductions(self, cr, uid, ids, context=None):
        res = {}
        payslip_line_obj = self.pool.get('hr.payslip.line')
        payslip_obj = self.pool.get('hr.payslip')
        employee_obj = self.pool.get('hr.employee')
        today = datetime.datetime.now()
        suma = 0.0

        # for month in xrange(1, 13):
        #    datemonthstart = "%s-%s-01" % (today.year, month)
        #    datemonthend = "%s-%s-%s" % (today.year, month, calendar.monthrange(today.year - 1, month)[1])

        #    datemonthstart = datetime.datetime.strptime(datemonthstart, "%Y-%m-%d")
        #    datemonthend = datetime.datetime.strptime(datemonthend, "%Y-%m-%d")

        #    slip_ids = payslip_obj.search(cr, uid, [('date_to', '>=', datemonthstart), ('date_to', '<=', datemonthend), ('employee_id', 'in', ids)])

        #    condition_slip_line = [('slip_id', 'in', slip_ids), ('code', '=', '039')]
        #    slip_line_ids = payslip_line_obj.search(cr, uid, condition_slip_line, order='code', context=False)

        #    for slip_browse in payslip_line_obj.browse(cr, uid, slip_line_ids, context=None):
        #        suma += slip_browse.amount

        # employee = employee_obj.browse(cr, uid, ids, context=None)
        # res[employee[0].id] = suma

        # return res

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
        'number_day_holidays': fields.integer('Number day holidays', size=2),
        'holidays_bonus': fields.integer('Holidays bonus', size=2),
        'december_salary_aprox': fields.float('December salary aprox'),
        'valor': fields.float('Other benefits deductions', size=7, digits=(5, 2)),
    }

    _defaults = {
        'withholding': 0,
        'salary': 0,
        'vat': ' ',
        'number_days_benefits': 60,
        'other_benefits_deductions': 0,
        'number_day_holidays': 15,
        'holidays_bonus': 15,
        'december_salary_aprox': 0,
        'valor': _get_total_deductions
    }
