#!/usr/bin/python
# -*- encoding: utf-8 -*-
###########################################################################
#    Copyright (C) 2015 thinkasoft , C.A. (www.thinkasoft.com)
#    All Rights Reserved
# ############## Credits ######################################################
#    Developed by: thinkasoft , C.A.
#
#    Coded by:  Gerardo Medina (gerardo.medina.m@gmail.com)
#               Aular Hector Manuel (aular.hector3@gmail.com)
#
##############################################################################


from openerp.osv import osv, fields


class hr_contract_trimestre(osv.Model):
    """Inherited hr.contract"""

    _inherit = 'hr.contract'

    _columns = {
        'average_wage': fields.float('Sueldo Trimestral'),
    }

    _defaults = {
        'average_wage': 0,
    }
