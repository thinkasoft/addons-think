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
###########################################################################
#    Copyright (C) 2015 thinkasoft , C.A. (www.thinkasoft.com)
#    All Rights Reserved
# ############## Credits ######################################################
#    Developed by: thinkasoft , C.A.
#
#    Coded by:  Aular Hector Manuel (aular.hector3@gmail.com)
#
##############################################################################

from openerp.osv import osv, fields


class Payroll_extension(osv.Model):
    """Inherited res.partner"""

    _inherit = 'hr.employee'

    def _get_public_holidays(self, cr, uid, ids, field_names, arg=None, context=None):
        res = {}
        employee_obj = self.pool.get('hr.employee')
        holidays_obj = self.pool.get('hr.holidays')
        condition_holydays = [('employee_id', 'in', ids),
                              ('holiday_status_id', '=', 13),
                              ]

        holidays_ids = holidays_obj.search(cr, uid, condition_holydays)
        employee = employee_obj.browse(cr, uid, ids, context=None)
        if holidays_obj.browse(cr, uid, holidays_ids, context=None):
            holidays_browser = holidays_obj.browse(cr, uid, holidays_ids, context=None)[0]
            res[employee[0].id] = holidays_browser.public_holiday_days
        else:
            res[employee[0].id] = 0

        return res

    _columns = {
        'public_holidays': fields.function(_get_public_holidays, type='integer', string='Public holidays', readonly=True),
    }
