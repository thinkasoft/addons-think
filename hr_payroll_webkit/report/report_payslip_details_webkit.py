#!/usr/bin/python
# -*- encoding: utf-8 -*-
###########################################################################
#    Copyright (C) 2015 thinkasoft , C.A. (www.thinkasoft.com)
#    All Rights Reserved
# ############## Credits ######################################################
#    Developed by: thinkasoft , C.A.
#
#    Coded by:  Aular Hector Manuel (aular.hector3@gmail.com)
#
##############################################################################

from openerp.report import report_sxw


class payslip_details_report(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(payslip_details_report, self).__init__(cr, uid, name, context)
        self.localcontext.update({
            'get_details_by_rule_category': self.get_details_by_rule_category,
            'get_lines_by_contribution_register': self.get_lines_by_contribution_register,
        })

    def get_details_by_rule_category(self, obj):
        payslip_line = self.pool.get('hr.payslip.line')
        rule_cate_obj = self.pool.get('hr.salary.rule.category')

        def get_recursive_parent(rule_categories):
            if not rule_categories:
                return []
            if rule_categories[0].parent_id:
                rule_categories.insert(0, rule_categories[0].parent_id)
                get_recursive_parent(rule_categories)
            return rule_categories

        res = []
        result = {}
        ids = []

        for id in range(len(obj)):
            ids.append(obj[id].id)
        if ids:
            self.cr.execute('''SELECT pl.id, pl.category_id FROM hr_payslip_line as pl \
                LEFT JOIN hr_salary_rule_category AS rc on (pl.category_id = rc.id) \
                WHERE pl.id in %s \
                GROUP BY rc.parent_id, pl.sequence, pl.id, pl.category_id \
                ORDER BY pl.sequence, rc.parent_id''', (tuple(ids),))
            for x in self.cr.fetchall():
                result.setdefault(x[1], [])
                result[x[1]].append(x[0])
            for key, value in result.iteritems():
                rule_categories = rule_cate_obj.browse(self.cr, self.uid, [key])
                parents = get_recursive_parent(rule_categories)
                category_total = 0
                for line in payslip_line.browse(self.cr, self.uid, value):
                    category_total += line.total
                level = 0
                for parent in parents:
                    res.append({
                        'rule_category': parent.name,
                        'name': parent.name,
                        'code': parent.code,
                        'level': level,
                        'total': category_total,
                    })
                    level += 1
                for line in payslip_line.browse(self.cr, self.uid, value):
                    res.append({
                        'rule_category': line.name,
                        'name': line.name,
                        'code': line.code,
                        'total': line.total,
                        'level': level
                    })
        return res

    def get_lines_by_contribution_register(self, obj):
        payslip_line = self.pool.get('hr.payslip.line')
        result = {}
        res = []

        for id in range(len(obj)):
            if obj[id].register_id:
                result.setdefault(obj[id].register_id.name, [])
                result[obj[id].register_id.name].append(obj[id].id)
        for key, value in result.iteritems():
            register_total = 0
            for line in payslip_line.browse(self.cr, self.uid, value):
                register_total += line.total
            res.append({
                'register_name': key,
                'total': register_total,
            })
            for line in payslip_line.browse(self.cr, self.uid, value):
                res.append({
                    'name': line.name,
                    'code': line.code,
                    'quantity': line.quantity,
                    'amount': line.amount,
                    'total': line.total,
                })
        return res



report_sxw.report_sxw('report.paylip.details.webkit', 'hr.payslip', 'hr_payroll_webkit/report/report_payslip_details_webkit.mako', parser=payslip_details_report)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
