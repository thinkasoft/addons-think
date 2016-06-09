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
    'name': "Account Report invoice line suppliers",
    'category': "Accounting & Finance",
    'version': "1.0",
    'depends': [
        "account",
        "l10n_ve_withholding_iva",
    ],
    'author': "Ingenieria Thinkasoft de Venezuela",
    'description': """ """,
    'website': 'http://www.thinkasoft.com',
    'data': [
        'report/customer_print_vat_report.xml',
        'views/customer_print_vat.xml',
    ],
    'installable': True,
}
