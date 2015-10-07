from openerp.osv import osv, fields


class Payroll_extension(osv.Model):
    """Inherited res.partner"""

    _inherit = 'hr.employee'

    _columns = {
        'vat': fields.char('Vat', size=12, required=True),
        'withholding': fields.float('Income Withholding', size=5, digits=(2, 2), required=True),
        'salary': fields.float('Monthly salary', required=True),
        'admission_date': fields.date('Date Admission', required=True),
        'date_exit': fields.date('Date Diacharge', required=False),
        'employment_benefit': fields.boolean('Employment Benefit?'),
        'reference_bank': fields.char('Reference Bank', size=50),
    }

    _defaults = {
        'withholding': 0,
        'salary': 0,
        'vat': ' ',
        'admission_date': fields.date.context_today,
    }
