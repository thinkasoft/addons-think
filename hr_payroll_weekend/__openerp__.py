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
{
    'name': "Calculation Monday and weekends",
    'category': "Human Resources",
    'version': "1.0",
    'depends': [
        "hr_payroll"
    ],
    'author': "Ingenieria Thinkasoft de Venezuela",
    'description': """
Calculation weekends and Mondays
================================
    Calculate weekends and Mondays from a period of time.

    fields:

    date_from: start day of payroll to generate.
    date_to: end day of payroll to generate.
""",
    'website': 'http://www.thinkasoft.com',
    'update_xml': ["view/hr_payroll_weekend.xml"],
    'installable': True,
}
