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
from openerp.tools.translate import _
from openerp.osv import osv


class line_report_suppliers(osv.osv_memory):
    _name = 'line_report_suppliers'
    _description = 'Print all lines of suppliers'
    _inherit = 'hr.attendance.week'

    def print_report(self, cr, uid, ids, context=None):
        """
            Gets the data in the view and validates if range is right
        """
        datas = dict(
            ids=context.get('active_ids', []),  # id the view current
            active_ids=context['active_ids'],  # id the view current
            model='res.partner',  # model current
            form=self.read(cr, uid, ids, [], context=context)[0]  # Data of the
                                                                  # view
        )

        # Gets field init_date and converted in Date format
        start_date = datetime.datetime.strptime(
            datas['form']['init_date'],
            "%Y-%m-%d"
        ).date()

        # Gets field end_date and converted in Date format
        stop_date = datetime.datetime.strptime(
            datas['form']['end_date'],
            "%Y-%m-%d"
        ).date()

        date_range = stop_date - start_date

        # Validates if:
        #   start_date < stop_date
        #   the range will not exceed one year
        #   Nota: works with leap-year
        if date_range.days < 1:
            raise osv.except_osv(
                _('Incorrect range!'),
                _('Starting Date is greater than Ending Date!')
            )

        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'line.report.suppliers',
            'datas': datas,
        }

line_report_suppliers()
