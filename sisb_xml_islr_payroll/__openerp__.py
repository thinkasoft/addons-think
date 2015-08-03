#!/usr/bin/python
# -*- encoding: utf-8 -*-
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
    "update_xml": [
        'view/xml_islr_payroll_view.xml',
        'view/xml_islr_payroll_view_extended.xml',
        'report/islr_wh_report.xml',
    ],
    "installable": True,
}
