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
