# -*- coding: utf-8 -*-
# Copyright 2016 Aular Hector Manuel <aular.hector3@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import time
from openerp.report import report_sxw
from openerp.osv import osv
import openerp.pooler
from openerp.tools.translate import _


class wh_muni_report_invetran(report_sxw.rml_parse):

    _inherit = "wh.muni.report"

    def __init__(self, cr, uid, name, context):
        """ Call __init__ l10n_ve_withholding_muni """
        super(wh_muni_report_invetran, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'get_atribute': self._get_atribute,
        })

    def _get_atribute(self):
        """ Get Tax Unit"""
        obj_l10n_ut = self.pool.get('l10n.ut')
        id_l10n_ut = obj_l10n_ut.search(self.cr, self.uid, [])
        unidad_tri = obj_l10n_ut.browse(self.cr, self.uid, id_l10n_ut)[0]
        unidad_tributaria = str(unidad_tri.amount)
        return unidad_tributaria

report_sxw.report_sxw(
    'report.wh.muni.report.invetran',
    'account.wh.munici',
    rml='retencion_municipal_invetran/views/wh_muni_report_invetran.rml',
    parser=wh_muni_report_invetran,
)
