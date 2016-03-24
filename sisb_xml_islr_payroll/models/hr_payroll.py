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

from openerp.osv import osv, fields


class hr_payslip(osv.osv):
    '''
    Payslip Line
    '''
    _inherit = 'hr.payslip'

    def _get_vat_fnc(self, cr, uid, ids, field_names, arg=None, context=None):
        res = {}
        for hr_payslip_obj in self.browse(cr, uid, ids, context=context):
            res[hr_payslip_obj.id] = hr_payslip_obj.employee_id.vat

        return res

    def _get_withholding_fnc(self, cr, uid, ids, field_names, arg=None,
                             context=None):
        res = {}
        for hr_payslip_obj in self.browse(cr, uid, ids, context=context):
            res[hr_payslip_obj.id] = hr_payslip_obj.employee_id.withholding

        return res

    def _get_ret_isrl_fnc(self, cr, uid, ids, field_names, arg=None,
                          context=None):
        hr_payslip_line_obj = self.pool.get('hr.payslip.line')
        res = {}
        for hr_payslip in self.browse(cr, uid, ids, context=context):
            hr_payslip_line_ids = hr_payslip_line_obj.search(
                cr, uid, [('slip_id', '=', hr_payslip.id),
                          ('name', '=', 'TOTAL ASIGNACIONES')], context=context
            )

            if hr_payslip_line_ids:

                hr_payslip_bwr = hr_payslip_line_obj.browse(
                    cr, uid, hr_payslip_line_ids, context=context
                )
                res[hr_payslip.id] = hr_payslip_bwr[0].amount
            else:
                res[hr_payslip.id] = 0
        return res

    _columns = {
        'islr_xml_wh_line_payroll_id': fields.many2one(
            'islr.xml.wh.doc', 'ISLR XML Document Payroll',
            help="Income tax XML Doc Payroll",),
        'concept_id': fields.many2one(
            'islr.wh.concept', 'Withholding Concept',
            help="Withholding concept associated with this rate",
            required=True),
        'rate_id': fields.many2one(
            'islr.rates', 'Person Type',
            domain="[('concept_id','=',concept_id)]", required=False,
            help="Person type"),
        'partner_vat': fields.function(_get_vat_fnc, type="char",
                                       string='VAT'),
        'total_amount': fields.function(
            _get_ret_isrl_fnc, type="float", string='Total amount'
        ),
        'withholding': fields.function(
            _get_withholding_fnc, type="float", string='Tasa Ret ISRl'
        ),
    }

    _defaults = {
    }
hr_payslip()
