#!/usr/bin/python
# -*- encoding: utf-8 -*-
###########################################################################
#    Copyright (C) thinkasoft , C.A. (www.thinkasoft.com)
#    All Rights Reserved
# ############## Credits ######################################################
#    Developed by: thinkasoft , C.A.
##############################################################################

from openerp.osv import fields, osv
import pdb


class hr_payslip_extended(osv.osv):

    _name = 'hr.payslip.extended'
    _columns = {
        'period_id': fields.many2one(
            'account.period', 'Period', readonly=False,
            help="Period when the accounts entries were done"),
    }
    _defaults = {
    }

    def on_change_method(self, cr, uid, period_id, context=None):
        context = {}

        obj_hp = self.pool.get('hr.payslip')
        obj_hp_line = self.pool.get('hr.payslip.line')
        lista = obj_hp.search(
            cr, uid,
            [("period_id", "=", period_id)],
            order="employee_id", context=context
        )
        brw = obj_hp_line.browse(cr, uid, lista, context=context)

        return {}
hr_payslip_extended()
