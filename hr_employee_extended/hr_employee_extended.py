from openerp.osv import osv, fields


class Payroll_extension(osv.Model):
    """Inherited res.partner"""

    _inherit = 'hr.employee'

    _columns = {
        'rif': fields.char('RIF', size=12, required=True),
        'retencion': fields.float('Rentencion de ISRL', size=5, digits=(2, 2),
                                  required=True),
        'sueldo': fields.float('Salario Mensual', required=True),
        'Fecha_Ingreso': fields.date('Fecha de Ingreso', required=True),
        'Fecha_Egreso': fields.date('Fecha de Egreso', required=False),
        'Beneficio_laboral': fields.boolean('Beneficio Laboral?'),
        'Constancia_banco': fields.char('Nombre de Banco', size=50),
    }

    _defaults = {
        'retencion': 0,
    }
