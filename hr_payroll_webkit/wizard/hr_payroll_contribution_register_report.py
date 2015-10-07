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


from openerp.osv import osv


class payslip_lines_contribution_register(osv.osv_memory):

    _inherit = 'payslip.lines.contribution.register'

    def print_report(self, cr, uid, ids, context=None):
        datas = {
            'ids': context.get('active_ids', []),
            'model': 'hr.contribution.register',
            'form': self.read(cr, uid, ids, [], context=context)[0]
        }
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'contribution.register.lines.webkit',
            'datas': datas,
        }

payslip_lines_contribution_register()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
