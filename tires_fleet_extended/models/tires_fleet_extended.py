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
#    Coded by:  Gerardo Medina gerardo.medina.m@gmail.com
#               Aular Hector Manuel (aular.hector3@gmail.com)
##############################################################################

from openerp.osv import osv, fields


class tires_fleet_extended(osv.Model):
    """Inherited fleet.vehicle"""

    _inherit = 'fleet.vehicle'

    _columns = {
        'marca': fields.char('Marca del Caucho', size=20),
        'modelo': fields.char('Modelo del Caucho', size=20),
        'medida': fields.char('Medida del Caucho'),
        'Fecha_Rotacion': fields.date('Fecha Rotacion'),
        'Posicion_actual': fields.char('Posicion Actual'),
    }

    _defaults = {
        'marca': "...",
    }
