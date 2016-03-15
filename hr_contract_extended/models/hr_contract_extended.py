# !/usr/bin/python
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
#    Copyright (C) 2015 thinkasoft , C.A. (www.thinkasoft.com)
#    All Rights Reserved
# ############## Credits ######################################################
#    Developed by: thinkasoft , C.A.
#    Coded by: Aular Hector Manuel (aular.hector3@gmail.com)
##############################################################################

from openerp.osv import osv, fields


class Contract_extension(osv.Model):
    """Inherited hr.contract"""

    _inherit = 'hr.contract'

    _columns = {
        'nhs_wh': fields.selection((('1', 'Weekly'), ('2', 'Biweekly'),
                                   ('3', 'Monthly')), 'NHS wh',
                                   required=False),
        'lph_wh': fields.selection((('1', 'Weekly'), ('2', 'Biweekly'),
                                   ('3', 'Monthly')), 'Lph wh',
                                   required=False),
        'income_wh': fields.selection((('1', 'Weekly'), ('2', 'Biweekly'),
                                      ('3', 'Monthly')), 'Income wh',
                                      required=False),
        'mod_income_wh': fields.float('Perc Income wh', digits=(2, 2),
                                      required=False),
        'insurance_health_wh': fields.selection((('1', 'Weekly'),
                                                ('2', 'Biweekly'),
                                                ('3', 'Monthly')),
                                                'Insurance health wh',
                                                required=False),
        'mod_insurance_health_wh': fields.float('Perc Insurance health wh',
                                                digits=(2, 2), required=False),
        'inces_wh': fields.boolean('Inces wh', required=False),
        'saving_wh': fields.selection((('1', 'Weekly'), ('2', 'Biweekly'),
                                      ('3', 'Monthly')), 'Saving wh ',
                                      required=False),
        'mod_saving_wh': fields.float('Perc Saving wh', digits=(2, 2),
                                      required=False),
    }

Contract_extension()
