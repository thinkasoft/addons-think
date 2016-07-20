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
    'name': "Contract extension",
    'category': "Human Resources",
    'version': "1.0",
    'depends': [
        "hr",
        "hr_contract",
    ],
    'author': "Ingenieria Thinkasoft de Venezuela",
    'description': """
Module Contract extension
====================================
add a new tab in the contract module, it contains:
--------------------------------------------------
    - Income wh
    - Insurance health wh
    - Perc Insurance health wh
    - Inces wh
    - Perc Saving wh
""",
    'website': 'http://www.thinkasoft.com',
    'data': ["views/hr_contract_extended.xml"],
    'installable': True,
}
