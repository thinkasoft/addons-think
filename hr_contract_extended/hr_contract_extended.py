from openerp.osv import osv, fields

class Contract_extension( osv.Model ):
	"""Inherited hr.contract"""

	_inherit = 'hr.contract'

	_columns = {
		'ret_ivss': fields.selection((('1','Mensuales'),('2','Quincenales'),('3','Semanales')),'Ret. de IVSS', required=False),
		'ret_faov': fields.selection((('1','Mensuales'),('2','Quincenales'),('3','Semanales')),'Ret. de FAOV', required=False),
		'ret_isrl': fields.selection((('1','Mensuales'),('2','Quincenales'),('3','Semanales')),'Ret. de ISRL', required=False),
		'mod_ret_isrl': fields.float(' M de Ret. ISRL',digits=(2,2), required=False),
		'ret_seguro_privado': fields.selection((('1','Mensuales'),('2','Quincenales'),('3','Semanales')),'Ret. de Seguro privado', required=False),
		'mod_ret_seguro_privado': fields.float(' MOD de Ret. seguro privado',digits=(2,2), required=False),
		'ret_inces': fields.boolean('Ret. de INCES', required=False),
		'ret_caja_ahorro': fields.selection((('1','Mensuales'),('2','Quincenales'),('3','Semanales')),'Ret. de CAJA DE AHORRO', required=False),
		'mod_ret_caja_ahorro': fields.float(' MOD de Ret. CAJA DE AHORRO',digits=(2,2), required=False),
	}


Contract_extension()
