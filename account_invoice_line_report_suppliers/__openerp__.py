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
        "report_webkit",
        "account",
        "account_invoice_line",
        "l10n_ve_fiscal_requirements",
        "hr_attendance",
    ],
    'author': "Ingenieria Thinkasoft de Venezuela",
    'description': """ """,
    'website': 'http://www.thinkasoft.com',
    'data': ['wizards/line_report_suppliers.xml',
             'report/report.xml'
             ],
    'installable': True,
}
