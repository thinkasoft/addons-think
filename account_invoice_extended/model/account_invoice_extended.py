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


class Account_invoice_extended (osv.Model):
    """
    Inherited account.invoice
    """
    _inherit = 'account.invoice'

    def onchange_reference(
        self, cr, uid, ids, supplier_invoice_number, context=None
    ):
        context = context or {}
        return {'value': {'reference': supplier_invoice_number, }}

Account_invoice_extended()
