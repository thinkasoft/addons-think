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
    'name': 'Nomina - Unir las retenciones de los empleados al archivo xml de \
    i slr ',
    'version': '0.1',
    'category': 'Contabilidad',
    'description': 'Incorpora las retenciones aplicadas a los trabajadores en\
    la generación del archivo xml de islr.',
    'author': 'Hector Manuel',
    'depends': [
                'l10n_ve_withholding_islr',
                'hr_payroll',
    ],
    "data": [
        'views/xml_islr_payroll_view.xml',
        'views/xml_islr_payroll_view_extended.xml',
        'report/islr_wh_report.xml',
    ],
    "installable": True,
}
