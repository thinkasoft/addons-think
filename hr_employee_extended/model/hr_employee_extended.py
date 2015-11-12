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

from openerp.osv import osv, fields


class Payroll_extension(osv.Model):
    """Inherited res.partner"""

    _inherit = 'hr.employee'

    _columns = {
        'vat': fields.char('Vat', size=12, required=True),
        'withholding': fields.float('Income Withholding', size=5, digits=(2, 2), required=True),
        'salary': fields.float('Monthly salary', required=True),
        'admission_date': fields.date('Date Admission', required=False),
        'date_exit': fields.date('Date Diacharge', required=False),
        'employment_benefit': fields.boolean('Employment Benefit?'),
        'reference_bank': fields.char('Reference Bank', size=50),
        'number_days_benefits': fields.integer('Number days benefits', size= 3),
        'other_benefits_deductions': fields.float('Other benefits deductions', size=7, digits=(5, 2), required=True),
    }

    _defaults = {
        'withholding': 0,
        'salary': 0,
        'vat': ' ',
        'number_days_benefits': 60,
        'other_benefits_deductions': 0
    }
