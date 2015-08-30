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
    'name': "Account invoice number extended",
    'category': "Accounting",
    'version': "1.0",
    'depends': [
        "account"
    ],
    'author': "Ingenieria Thinkasoft de Venezuela",
    'description': """
Accounting invoice extended module adds:
----------------------------------------
* Modifies field: supplier_invoice_number located in Accounting -> Suppliers -> Suppliers invoices. it's being added a method onchange_reference.

    * Method onchange_reference: assigns the field "reference" the same information that contain's supplier_invoice_number.
""",
    'website': 'http://www.thinkasoft.com',
    'update_xml': ["view/account_invoice_extended.xml"],
    'installable': True,
}
