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
    'name': "Contract trimestre extension",
    'category': "Human Resources",
    'version': "1.0",
    'depends': [
                "hr_contract"],
    'author': "Ingenieria Thinkasoft de Venezuela",
    'description': """
Add field Quarterage to IVSS calculate
==============================================
fields added:
-------------
  - Quarterage [Text]""",
    'data': [
              'views/hr_contract_trimestre.xml'],
}
