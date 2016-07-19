# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2011-2013 Serpent Consulting Services (<http://www.serpentcs.com>)
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
############################################################################

import time
from datetime import datetime
from dateutil import relativedelta

from openerp.osv import fields, osv

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
            'report_name': 'contribution.register.lines.webkit.inces',
            'datas': datas,
        }

payslip_lines_contribution_register()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
