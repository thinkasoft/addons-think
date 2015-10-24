#!/usr/bin/python
# -*- encoding: utf-8 -*-
###########################################################################
#    Copyright (C) 2015 thinkasoft , C.A. (www.thinkasoft.com)
#    All Rights Reserved
# ############## Credits ######################################################
#    Developed by: thinkasoft , C.A.
#
#    Coded by:  Gerardo Medina gerardo.medina.m@gmail.com
#               Aular Hector Manuel (aular.hector3@gmail.com)
#
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
