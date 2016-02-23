from datetime import datetime
from dateutil.relativedelta import relativedelta

from openerp.osv import fields, osv

class hr_employee_report_wizard_benefits_employee(osv.osv_memory):
    _name = 'hr.employee.report.wizard.benefits.employee'
    _description = 'Print Week Attendance Report'
    _inherit = 'hr.attendance.week'

    def print_report(self, cr, uid, ids, context=None):
        datas = {
            'ids': context.get('active_ids', []),
            'active_ids': context['active_ids'],
            'model': 'hr.employee',
            'form': self.read(cr, uid, ids, [], context=context)[0]
        }
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'hr.employee.report.benefits.employee',
            'datas': datas,
        }

hr_employee_report_wizard_benefits_employee()
