# !/usr/bin/python
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
##############################################################################
#    Copyright (C) 2015 thinkasoft , C.A. (www.thinkasoft.com)
#    All Rights Reserved
# ############## Credits ######################################################
#    Developed by: thinkasoft , C.A.
#    Coded by: Aular Hector Manuel (aular.hector3@gmail.com)
##############################################################################

from openerp.osv import osv
from datetime import datetime
from dateutil import rrule
from openerp.tools.translate import _


class HrPayrollWeekend(osv.osv):
    '''
    Payslip Weekend
    '''
    _inherit = 'hr.payslip'

    # Caculate weekend and Mondays
    def calculate_weekend(self, cr, uid, ids, date_from, date_to, contract_ids, context=None):
        weekend = [5, 6]
        weekend2 = [0, 6]
        sunday = [0]

        for contract in self.pool.get('hr.contract').browse(cr, uid, [contract_ids], context=context):

            date_from = datetime.strptime(date_from, "%Y-%m-%d")
            date_to = datetime.strptime(date_to, "%Y-%m-%d")

            totalweekemd = rrule.rrule(rrule.DAILY, dtstart=date_from, until=date_to, byweekday=weekend)
            totalweekemd2 = rrule.rrule(rrule.DAILY, dtstart=date_from, until=date_to, byweekday=weekend2)
            totalsunday = rrule.rrule(rrule.DAILY, dtstart=date_from, until=date_to, byweekday=sunday)

            res = []
            attendances_weekend = {
                'name': _('Not Working days paid at 100% (Saturday - Sunday)'),
                'sequence': 1,
                'code': 'Weekend',
                'number_of_days': totalweekemd.count(),
                'number_of_hours': 0.0,
                'contract_id': contract.id,
            }

            attendances_weekend2 = {
                'name': _('Not Working days paid at 100% (Sunday - Monday)'),
                'sequence': 1,
                'code': 'Weekend2',
                'number_of_days': totalweekemd2.count(),
                'number_of_hours': 0.0,
                'contract_id': contract.id,
            }

            attendances_sunday = {
                'name': _('Monday'),
                'sequence': 1,
                'code': 'Monday',
                'number_of_days': totalsunday.count(),
                'number_of_hours': 0.0,
                'contract_id': contract.id,
            }

            res = [attendances_weekend]
            res += [attendances_weekend2]
            res += [attendances_sunday]
        return res

    def calculate_other(self, cr, uid, contract_ids, date_from, date_to, context=None):
        inputs = []
        for contract in self.pool.get('hr.contract').browse(cr, uid, [contract_ids], context=context):
            employee_obj = self.pool.get('hr.employee')
            expenses = {}
            profits = {}
            number_day_holidays = {}
            holidays_bonus = {}
            salary_yearly = employee_obj._get_total_deductions(cr, uid, [contract.employee_id.id], context)
            profits = {
                'name': _('Profits'),
                'code': 'Profits',
                'amount': salary_yearly[contract.employee_id.id],
                'contract_id': contract.id,
            }
            number_day = employee_obj._calc_days(cr, uid, [contract.employee_id.id], context)
            number_day_holidays = {
                'name': _('Number day holidays'),
                'code': 'number_day_holidays',
                'amount': number_day[contract.employee_id.id],
                'contract_id': contract.id,
            }
            holidays_bonus = {
                'name': _('Holidays bonus'),
                'code': 'holidays_bonus',
                'amount': number_day[contract.employee_id.id],
                'contract_id': contract.id,
            }
            expenses = {
                'name': _('Expenses'),
                'code': 'Expenses',
                'amount': 0.0,
                'contract_id': contract.id,
            }
            difference = {
                'name': _('Payment Difference'),
                'code': 'Difference',
                'amount': 0.0,
                'contract_id': contract.id,
            }
            otherincomes = {
                'name': _('Otherincomes'),
                'code': 'Otherincomes',
                'amount': 0.0,
                'contract_id': contract.id,
            }

            anticipio_advance = {
                'name': _('Advance of salary'),
                'code': 'Advance',
                'amount': 0.0,
                'contract_id': contract.id,
            }

            inputs += [difference] + [otherincomes] + [anticipio_advance] + [expenses] + [profits] + [number_day_holidays] + [holidays_bonus]

        return inputs

    # Replace method onchange_employee_id located in hr_payroll line 641
    def onchange_employee_id_1(self, cr, uid, ids, date_from, date_to, employee_id=False, contract_id=False, context=None):
        res = super(HrPayrollWeekend, self).onchange_employee_id(cr, uid, ids, date_from, date_to, employee_id, contract_id, context)

        if not contract_id:
            contract_id = res['value']['contract_id']
        weekend_id = self.calculate_weekend(cr, uid, ids, date_from, date_to, contract_id, context)
        other_line = self.calculate_other(cr, uid, contract_id, date_from, date_to, context)

        res['value']['worked_days_line_ids'] += weekend_id
        res['value']['input_line_ids'] += other_line

        return res

    # Replace method onchange_contract_id located in hr_payroll 712
    def onchange_contract_id_1(
        self, cr, uid, ids, date_from, date_to, employee_id=False,
        contract_id=False, context=None
    ):
        if context is None:
            context = {}
        res = {'value': {
            'line_ids': [],
            'name': '', }
        }
        context.update({'contract': True})
        if not contract_id:
            res['value'].update({'struct_id': False})
        return self.onchange_employee_id_1(cr, uid, ids, date_from=date_from, date_to=date_to, employee_id=employee_id, contract_id=contract_id, context=context)

HrPayrollWeekend()
