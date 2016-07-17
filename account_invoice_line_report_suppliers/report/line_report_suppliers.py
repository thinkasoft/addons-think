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


class line_report_suppliers(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(line_report_suppliers, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'get_supplier_invoice_line': self._get_supplier_invoice_line,
        })

    def set_context(self, objects, data, ids, report_type=None):
        """
          It obtains the information deposited the wizard and 
          they are assigned to the variable context to be used in the report.
          @param data: contain the information entered in the wizard.
          @return: update the variably context with the new dates.
        """
        # Gets field init_date and converted in Date format
        start_date = datetime.datetime.strptime(
            data.get('form').get('init_date'), "%Y-%m-%d")
        stop_date = datetime.datetime.strptime(
            data.get('form').get('end_date'), "%Y-%m-%d")

        # assigned to the variable context
        self.localcontext.update({
            'start_date': start_date,
            'stop_date': stop_date,
        })

        return super(line_report_suppliers, self).set_context(
            objects, data, ids, report_type=report_type)

    def _get_supplier_invoice_line(self, start_days, stop_days, obj):
        """
          All the lines of sales are obtained in this which involved the selected client
          @param obj: Employe object used currently.
          @param start_days: date init used for the search.
          @param stop_days: date stop used for the search.
          @return: update the variably context with the new dates.
        """
        res = list()
        dic = dict()
        account_invoice_obj = self.pool.get('account.invoice')

        # Declaring condition to realize search
        account_invoice_condition = [('date_document', '>=', start_days),
                                     ('date_document', '<=', stop_days), ('state', '=', 'paid')]

        # It returns all the id that fulfill the condition.
        account_invoice_ids = account_invoice_obj.search(self.cr, self.uid, account_invoice_condition, context=False)
        for account_invoice_line in account_invoice_obj.browse(self.cr, self.uid, account_invoice_ids, context=None):
            # For every line it is necessary to validate if this belongs to the corresponding client
            for invoice_line in account_invoice_line.invoice_line:
                if invoice_line.partner_other_id.id == obj.id:
                    # If the line belongs to the client the information and guard must be obtained in res
                    dic = dict(name_supplier=invoice_line.partner_id.name,
                               name_product=invoice_line.name,
                               sub_total=invoice_line.price_subtotal,
                               price_unit=invoice_line.price_unit,
                               quantity=invoice_line.quantity,
                               iva_amount=invoice_line.invoice_line_tax_id[0].amount,
                               iva_description=invoice_line.invoice_line_tax_id[0].description,)
                    res.append(dic)
        return res

report_sxw.report_sxw('report.line.report.suppliers',
                      'res.partner',
                      'account_invoice_line_report_suppliers/report/line_report_suppliers.mako',
                      parser=line_report_suppliers)
