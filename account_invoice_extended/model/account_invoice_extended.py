from openerp.osv import osv, fields

class Account_invoice_extended( osv.Model ):
	"""Inherited account.invoice"""

	_inherit = 'account.invoice'

	def onchange_reference(self, cr, uid, ids, supplier_invoice_number, context=None):

		context = context or {}

		return {'value': {'reference': supplier_invoice_number, }}

Account_invoice_extended()