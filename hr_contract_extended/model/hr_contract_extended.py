from openerp.osv import osv, fields

class Contract_extension( osv.Model ):
	"""Inherited hr.contract"""

	_inherit = 'hr.contract'

	_columns = {
		'nhs_wh': fields.selection((('1','Weekly'),('2','Biweekly'),('3','Monthly')),'NHS wh', required=False),
		'lph_wh': fields.selection((('1','Weekly'),('2','Biweekly'),('3','Monthly')),'Lph wh', required=False),
		'income_wh': fields.selection((('1','Weekly'),('2','Biweekly'),('3','Monthly')),'Income wh', required=False),
		'mod_income_wh': fields.float('Perc Income wh',digits=(2,2), required=False),
		'insurance_health_wh': fields.selection((('1','Weekly'),('2','Biweekly'),('3','Monthly')),'Insurance health wh', required=False),
		'mod_insurance_health_wh': fields.float('Perc Insurance health wh',digits=(2,2), required=False),
		'inces_wh': fields.boolean('Inces wh', required=False),
		'saving_wh': fields.selection((('1','Weekly'),('2','Biweekly'),('3','Monthly')),'Saving wh ', required=False),
		'mod_saving_wh': fields.float('Perc Saving wh',digits=(2,2), required=False),
	}


Contract_extension()