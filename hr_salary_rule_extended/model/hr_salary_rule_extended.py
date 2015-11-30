#!/usr/bin/python
# -*- encoding: utf-8 -*-
###########################################################################
#    Copyright (C) 2015 thinkasoft , C.A. (www.thinkasoft.com)
#    All Rights Reserved
# ############## Credits ######################################################
#    Developed by: thinkasoft , C.A.
#    Coded by: Aular Hector Manuel (aular.hector3@gmail.com)
##############################################################################

from openerp.osv import osv


class HrSalaryRule (osv.Model):
    _inherit = 'hr.salary.rule'

    def onchange_sequence(
        self, cr, uid, ids, code, context=None
    ):
        context = context or {}
        return {'value': {'sequence': int(code), }}

HrSalaryRule()
