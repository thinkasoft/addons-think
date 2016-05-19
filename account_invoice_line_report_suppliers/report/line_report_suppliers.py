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
from openerp.report import report_sxw
from openerp.tools.translate import _


class line_report_suppliers(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(line_report_suppliers, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'get_supplier_invoice_line': self._get_supplier_invoice_line,
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

        return super(line_report_suppliers, self).set_context(
            objects, data, ids, report_type=report_type)

    def _get_supplier_invoice_line(self, start_days, stop_days, obj):
        res = list()
        invoice_line_obj = self.pool.get('account.invoice.line')
        invoice_line_condition = [('partner_other_id', '=', obj.id)]
        invoice_line_ids = invoice_line_obj.search(self.cr, self.uid, invoice_line_condition, context=False)

        for invoice_line in invoice_line_obj.browse(self.cr, self.uid, invoice_line_ids, context=None):
            dic = dict(name_supplier=invoice_line.partner_id.name,
                       name_product=invoice_line.name,
                       sub_total=invoice_line.price_subtotal,
                       quantity=invoice_line.quantity,
                       iva_amount=invoice_line.invoice_line_tax_id[0].amount,
                       iva_description=invoice_line.invoice_line_tax_id[0].description,)
            print dic
            res.append(dic)
        return res

report_sxw.report_sxw('report.line.report.suppliers',
                      'res.partner',
                      'account_invoice_line_report_suppliers/report/line_report_suppliers.mako',
                      parser=line_report_suppliers)
