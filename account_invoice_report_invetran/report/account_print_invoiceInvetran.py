# -*- coding: utf-8 -*-
# Copyright 2016 Aular Hector Manuel <aular.hector3@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import time
from openerp.report import report_sxw


class account_invoice(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        """ Init object for the report report_invoice_invetran """
        super(account_invoice, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
        })
report_sxw.report_sxw(
    'report.account.invoice_invetran',
    'account.invoice',
    'account_invoice_report_invetran/report/report_invoice_invetran.rml',
    parser=account_invoice
)
