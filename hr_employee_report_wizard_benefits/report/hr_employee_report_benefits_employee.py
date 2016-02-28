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

    global list_month_es
    list_month_es = list(['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo',
                          'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre',
                          'Noviembre', 'Diciembre'])

    def __init__(self, cr, uid, name, context):
        super(HrEmployeeReportBenefitsEmployee, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'get_payslip_lines': self._get_payslip_lines,
        })

    def set_context(self, objects, data, ids, report_type=None):
        """Populate a ledger_lines attribute on each browse record that will
           be used by mako template"""

        start_date = datetime.datetime.strptime(
            data.get('form').get('init_date'), "%Y-%m-%d").date()
        stop_date = datetime.datetime.strptime(
            data.get('form', {}).get('end_date'), "%Y-%m-%d").date()
        self.localcontext.update({
            'start_date': start_date,
            'stop_date': stop_date,
        })

        return super(HrEmployeeReportBenefitsEmployee, self).set_context(
            objects, data, ids, report_type=report_type)

    def _get_slip_line_ids(self, year, month, start_days, stop_days, obj):
        payslip_line_obj = self.pool.get('hr.payslip.line')
        payslip_obj = self.pool.get('hr.payslip')

        if month == 12:
            return list()

        if start_days is not 0:
            datemonthstart = "%s-%s-%s" % (year, month, start_days)
        else:
            datemonthstart = "%s-%s-01" % (year, month)

        if stop_days is not 0:
            datemonthend = "%s-%s-%s" % (year, month, stop_days)
        else:
            datemonthend = "%s-%s-%s" % (year, month, calendar.monthrange(year, month)[1])

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
        return slip_line_ids

    def _calc_payslip_utilites(self, month, slip_line_ids):
        payslip_line_obj = self.pool.get('hr.payslip.line')
        dic = dict(month=list_month_es[month - 1],
                   basic=0,
                   integral=0,)

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
        return dic

    def _get_payslip_lines(self, obj, start_date, stop_date):
        res = list()

        if stop_date.year == start_date.year and stop_date.month == start_date.month:
            slip_line_ids = self._get_slip_line_ids(
                start_date.year,
                start_date.month,
                start_date.day,
                stop_date.day,
                obj)
            res.append(self._calc_payslip_utilites(start_date.month, slip_line_ids))
        else:
            if start_date.month != 12:
                slip_line_ids = self._get_slip_line_ids(
                    start_date.year,
                    start_date.month,
                    start_date.day,
                    0,
                    obj)
            else:
                slip_line_ids = list()
            res.append(self._calc_payslip_utilites(start_date.month, slip_line_ids))

            year_star = start_date.year
            month_star = start_date.month + 1
            month_end = 12 if year_star is not stop_date.year else stop_date.month

            while year_star <= stop_date.year:
                for month in xrange(month_star, month_end):
                    slip_line_ids = self._get_slip_line_ids(
                        year_star,
                        month,
                        0,
                        0,
                        obj)
                    res.append(self._calc_payslip_utilites(month, slip_line_ids))
                year_star += 1
                if month_end == 12:
                    month_star = 1
                    month_end = stop_date.month

            slip_line_ids = self._get_slip_line_ids(
                stop_date.year,
                stop_date.month,
                0,
                stop_date.day,
                obj)
            res.append(self._calc_payslip_utilites(stop_date.month, slip_line_ids))
        return res

report_sxw.report_sxw('report.hr.employee.report.benefits.employee',
                      'hr.employee',
                      'hr_employee_report_wizard_benefits/report/hr_employee_report_benefits_employee.mako',
                      parser=HrEmployeeReportBenefitsEmployee)
