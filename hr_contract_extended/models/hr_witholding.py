# -*- coding= utf-8 -*-
# Copyright 2016 Hector Manuel Aular <aular.hector3@gmail.com>
# License AGPL-3.0 or later (http=//www.gnu.org/licenses/agpl).

from openerp import models, fields


class HrWitholding(models.Model):

    _inherit = "hr.contract"

    option = ('1', 'Weekly'), ('2', 'Biweekly'), ('3', 'Monthly')

    cal_withol = fields.Selection(option, 'Withholding period')
    mod_income_wh = fields.Float('Perc Income wh',)
    mod_ins_health_wh = fields.Float('Perc Insurance health wh')
    mod_saving_wh = fields.Float('Perc Saving wh')
    inces_wh = fields.Boolean('Inces wh')
    average_wage = fields.Float('Quaterage')
