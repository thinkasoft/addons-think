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

import datetime
import calendar
from openerp.tools.translate import _
from openerp.osv import osv


class hr_employee_report_wizard_benefits_employee(osv.osv_memory):
    _name = 'hr.employee.report.wizard.benefits.employee'
    _description = 'Print Week Attendance Report'
    _inherit = 'hr.attendance.week'

    def print_report(self, cr, uid, ids, context=None):
        datas = {
            'ids': context.get('active_ids', []),
            'active_ids': context['active_ids'],
            'model': 'hr.employee',
            'form': self.read(cr, uid, ids, [], context=context)[0]
        }

        start_date = datetime.datetime.strptime(
            datas['form']['init_date'],
            "%Y-%m-%d"
        ).date()
        stop_date = datetime.datetime.strptime(
            datas['form']['end_date'],
            "%Y-%m-%d"
        ).date()

        date_range = stop_date - start_date
        if date_range.days < 1:
            raise osv.except_osv(_('Incorrect range!'), _('Starting Date is greater than Ending Date!'))
        elif date_range.days == 365:
            days_february_start = calendar.monthrange(start_date.year, 2)[1]
            days_february_stop = calendar.monthrange(stop_date.year, 2)[1]

            if start_date.month <= 2 and days_february_start == 28:
                raise osv.except_osv(_('Limit range!'), _('Limit range is 1 year!'))

            if stop_date.month >= 2 and days_february_stop == 28:
                raise osv.except_osv(_('Limit range!'), _('Limit range is 1 year!'))
        elif date_range.days > 364:
            raise osv.except_osv(_('Limit range!'), _('Limit range is 1 year!'))

        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'hr.employee.report.benefits.employee',
            'datas': datas,
        }

hr_employee_report_wizard_benefits_employee()
