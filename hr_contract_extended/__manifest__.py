# -*- coding: utf-8 -*-
# Copyright 2016 Héctor Manuel Aular Osorio <aular.hector3@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Hr contract witholding",
    "summary": "Agrega sección de retenciones en contratos",
    "version": "10.0",
    "category": "HR",
    "website": "http://www.thinkasoft.com",
    "author": "Héctor Manuel Aular Osorio, Ingenieria Thinkasoft de Venezuela",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "hr",
        "hr_contract",
    ],
    "data": [
        'views/hr_witholding.xml',
    ]
}
