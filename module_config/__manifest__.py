# -*- coding: utf-8 -*-
# Copyright 2016 Héctor Manuel Aular Osorio <aular.hector3@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Configuracion OVL",
    "summary": "Módulo para instalar toda las dependencias de la OVL",
    "version": "10.0",
    "category": "Config",
    "website": "http://www.thinkasoft.com",
    "author": "Héctor Manuel Aular Osorio, Ingenieria Thinkasoft de Venezuela",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends":
    [
        "base",
        "account",
        "hr",
        "hr_contract",
        "hr_payroll",
        "sale",
        "purchase",
        "fleet",
    ],
}
