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
from datetime import datetime
from dateutil import rrule


class HrPayrollWeekend(osv.osv):
    '''
    Payslip Weekend
    '''
    _inherit = 'hr.payslip'

    def calculate_weekend(self, cr, uid, ids, date_from, date_to, contract_ids, context=None):
        weekend = [5, 6]
        sunday = [0]

        contract = self.pool.get('hr.contract').browse(cr, uid, contract_ids, context=context)
        date_from = datetime.strptime(date_from, "%Y-%m-%d")
        date_to = datetime.strptime(date_to, "%Y-%m-%d")

        totalweekemd = rrule.rrule(rrule.DAILY, dtstart=date_from, until=date_to, byweekday=weekend)
        totalsunday = rrule.rrule(rrule.DAILY, dtstart=date_from, until=date_to, byweekday=sunday)

        res = []
        attendances_weekend = {
            'name': "Not Working days paid at 100%",
            'sequence': 1,
            'code': 'Weekend',
            'number_of_days': totalweekemd.count(),
            'number_of_hours': 0.0,
            'contract_id': contract.id,
        }

        attendances_sunday = {
            'name': "Lunes",
            'sequence': 2,
            'code': 'Lunes',
            'number_of_days': totalsunday.count(),
            'number_of_hours': 0.0,
            'contract_id': contract.id,
        }

        res = [attendances_weekend]
        res += [attendances_sunday]
        print res
        return res

    def onchange_employee_id_1(self, cr, uid, ids, date_from, date_to, employee_id=False, contract_id=False, context=None):
        res = super(HrPayrollWeekend, self).onchange_employee_id(cr, uid, ids, date_from, date_to, employee_id, contract_id, context)
        weekend_id = self.calculate_weekend(cr, uid, ids, date_from, date_to, contract_id, context)

        res['value']['worked_days_line_ids'] += weekend_id
        return res

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
