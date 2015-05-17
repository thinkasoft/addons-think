from openerp.osv import osv, fields

class Payroll_extension(osv.Model):
	"""Inherited res.partner"""

	_inherit = 'hr.employee'

	_columns = {

		'rif' : fields.char('RIF', size=12, required=True),
		'retencion' : fields.integer('Rentencion de ISRL', size=11 ,required=True),
	}


Payroll_extension()
