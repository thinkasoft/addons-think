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

import calendar
import datetime
from openerp.report import report_sxw
from openerp.tools.translate import _


class HrEmployeeReportBenefitsEmployee(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(HrEmployeeReportBenefitsEmployee, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'get_payslip_lines': self._get_payslip_lines,
        })

    def set_context(self, objects, data, ids, report_type=None):
        """Populate a ledger_lines attribute on each browse record that will
           be used by mako template"""
        start_date = data.get('form').get('init_date')
        stop_date = data.get('form', {}).get('end_date')

        self.localcontext.update({
            'start_date': start_date,
            'stop_date': stop_date,
        })

        return super(HrEmployeeReportBenefitsEmployee, self).set_context(
            objects, data, ids, report_type=report_type)

    def _get_payslip_lines(self, obj, start_date, stop_date):
        res = []
        dic = {}
        list_month_es = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo',
                         'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre',
                         'Noviembre', 'Diciembre']
        payslip_line_obj = self.pool.get('hr.payslip.line')
        payslip_obj = self.pool.get('hr.payslip')
        today = datetime.datetime.now()
        sum_integral = 0
        sum_holiday = 0
        for month in xrange(1, 13):
            slip_ids = []
            slip_line_ids = []

            if month < 12:
                    datemonthstart = "%s-%s-01" % (today.year, month)
                    datemonthend = "%s-%s-%s" % (today.year, month, calendar.monthrange(today.year, month)[1])

                    datemonthstart = datetime.datetime.strptime(datemonthstart, "%Y-%m-%d")
                    datemonthend = datetime.datetime.strptime(datemonthend, "%Y-%m-%d")

                    condition_slip = [('date_to', '>=', datemonthstart), ('date_to', '<=', datemonthend),
                                      ('employee_id', '=', obj.id),
                                      '|', ('state', '=', 'done'), ('state', '=', 'paid'),
                                      ]
                    slip_ids = payslip_obj.search(self.cr, self.uid, condition_slip, context=False)

                    slip_line_ids = payslip_line_obj.search(
                        self.cr, self.uid, [
                            ('slip_id', 'in', slip_ids), '|', '|', '|', '|', '|',
                            ('code', '=', '001'), ('code', '=', '003'), ('code', '=', '002'),
                            ('code', '=', '005'), ('code', '=', '009'), ('code', '=', '039')],
                        order='code', context=False
                    )

            dic = {
                'month': list_month_es[month - 1],
                'basic': 0,
                'integral': 0,
            }
            for slip_browse in payslip_line_obj.browse(self.cr, self.uid, slip_line_ids, context=None):
                sum_integral = 0
                sum_holiday = 0
                if slip_browse.code != '039':
                    if slip_browse.code != '009':
                        dic['basic'] += slip_browse.amount * slip_browse.quantity
                    else:
                        sum_holiday += slip_browse.quantity
                else:
                    dic['integral'] += slip_browse.amount
                    sum_integral += slip_browse.amount
            dic['integral'] += ((sum_holiday / 12) * (sum_integral / 30))
            res.append(dic)
        return res

report_sxw.report_sxw('report.hr.employee.report.benefits.employee',
                      'hr.employee',
                      'hr_employee_report_wizard_benefits/report/hr_employee_report_benefits_employee.mako',
                      parser=HrEmployeeReportBenefitsEmployee)
