# -*- coding: utf-8 -*-
# Base: Hector

from odoo import fields, models


class Survey(models.Model):
    _inherit = 'survey.page'

    def _compute_score_answers(self):
        for survey_page in self:
            domain = [('survey_id', '=', survey_page.survey_id.id), ('question_id', 'in', survey_page.question_ids.ids)]
            survey_page.survey_page_score = sum(self.env['survey.user_input_line'].search(domain).mapped('quizz_mark'))

    survey_page_score = fields.Float('Total score', compute=_compute_score_answers)