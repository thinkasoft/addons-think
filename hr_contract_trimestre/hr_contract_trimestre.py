from openerp.osv import osv, fields

class hr_contract_trimestre(osv.Model):
	"""Inherited hr.contract"""

	_inherit = 'hr.contract'

	_columns = {	
		'average_wage' : fields.float('Sueldo Trimestral'),
	}

	_defaults = {
	
		'average_wage' : 0,
}
