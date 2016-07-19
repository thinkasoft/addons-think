#!/usr/bin/python
# -*- encoding: utf-8 -*-
###########################################################################
#    Copyright (C) 2015 thinkasoft , C.A. (www.thinkasoft.com)
#    All Rights Reserved
# ############## Credits ######################################################
#    Developed by: thinkasoft , C.A.
#
#    Coded by:  Aular Hector Manuel (aular.hector3@gmail.com)
#
##############################################################################

import time
from openerp.osv import fields, osv
from datetime import datetime
from dateutil import relativedelta


class hr_payslip_extended(osv.osv):

    _name = 'hr.payslip.extended'
    _description = 'PaySlip Lines by Contribution Registers'
    _columns = {
        'date_from': fields.date('Date From', required=True),
        'date_to': fields.date('Date To', required=True),
    }

    _defaults = {
        'date_from': lambda *a: time.strftime('%Y-%m-01'),
        'date_to': lambda *a: str(datetime.now() +
                                  relativedelta.relativedelta(months=+1,
                                                              day=1,
                                                              days=-1))[:10],
    }

    def print_report(self, cr, uid, ids, context=None):

        datas = {
            'ids': context.get('active_ids', []),
            'model': 'hr.payslip.extended',
            'form': self.read(cr, uid, ids, [], context=context)[0]
        }
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'hr.payslip.extended.mako',
            'datas': datas,
        }
hr_payslip_extended()
