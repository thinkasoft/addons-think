#!/usr/bin/python
# -*- encoding: utf-8 -*-
###########################################################################
#    Copyright (C) thinkasoft , C.A. (www.thinkasoft.com)
#    All Rights Reserved
# ############## Credits ######################################################
#    Developed by: thinkasoft , C.A.
##############################################################################

from openerp.osv import fields, osv


class hr_payslip_extended(osv.osv):

    _name = 'hr.payslip.extended'
    _columns = {
        'period_id': fields.many2one(
            'account.period', 'Period', readonly=False,
            help="Period when the accounts entries were done"
        ),
    }
    _defaults = {
    }

hr_payslip_extended()
