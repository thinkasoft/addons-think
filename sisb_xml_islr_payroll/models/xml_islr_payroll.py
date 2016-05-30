# !/usr/bin/python
# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
#    Copyright (C) 2015 thinkasoft , C.A. (www.thinkasoft.com)
#    All Rights Reserved
# ############## Credits ######################################################
#    Developed by: thinkasoft , C.A.
#    Coded by: Aular Hector Manuel (aular.hector3@gmail.com)
##############################################################################

from osv import osv
from osv import fields
from tools.translate import _
import time
import datetime
from xml.etree.ElementTree import Element, SubElement, tostring


class islr_xml_wh_doc(osv.osv):
    _inherit = "islr.xml.wh.doc"

    _order = "id desc"

    _defaults = {
        'name': lambda self, cr, uid, context: _('Withholding Income ') +
        time.strftime('%m/%Y')
    }

    def _get_amount_total_payroll(self, cr, uid, ids, name, args,
                                  context=None):
        res = dict()
        for xml in self.browse(cr, uid, ids, context):
            res[xml.id] = 0.0
            for line in xml.xml_payroll_ids:
                division = float(line.withholding) / 100
                amount_total_payroll = division * line.total_amount
                res[xml.id] += amount_total_payroll
        return res

    def _get_amount_total_base_payroll(self, cr, uid, ids, name, args,
                                       context=None):
        res = dict()
        for xml in self.browse(cr, uid, ids, context):
            res[xml.id] = 0.0
            for line in xml.xml_payroll_ids:
                res[xml.id] += line.total_amount
        return res

    _columns = {
        'xml_ids': fields.one2many('islr.xml.wh.line', 'islr_xml_wh_doc',
                                   'XML Document Lines'),
        'xml_payroll_ids': fields.one2many('hr.payslip',
                                           'islr_xml_wh_line_payroll_id',
                                           'XML Document Payroll Lines'),
        'amount_total_ret_payroll': fields.function(
            _get_amount_total_payroll,
            method=True,
            digits=(16, 2),
            readonly=True,
            string='Withholding Income Amount Total for payroll',
            help="Amount Total of withholding - Payroll"),
        'amount_total_base_payroll': fields.function(
            _get_amount_total_base_payroll,
            method=True,
            digits=(16, 2),
            readonly=True,
            string='Without Tax Amount Total for payroll',
            help="Total without taxes - Payroll"),
    }

    # validar el proceso de confirmar
    def action_confirm2(self, cr, uid, ids, context={}):
        for xml_doc_brw in self.browse(cr, uid, ids, context=context):
            if not xml_doc_brw.xml_ids and not xml_doc_brw.xml_payroll_ids:
                raise osv.except_osv(
                    _('Error!'),
                    _("Retentions must be loaded before confirming"))

        return super(islr_xml_wh_doc, self).action_confirm1(cr, uid, ids,
                                                            context)

    def action_done2(self, cr, uid, ids, context=None):
        """ Passes the document to state done
        """
        context = context or dict()
        root = self._xml2(cr, uid, ids)
        self._write_attachment(cr, uid, ids, root, context)
        self.write(cr, uid, ids, {'state': 'done'})
        return True

    def _xml2(self, cr, uid, ids):
        # Modificaciones para extraer la fecha contable de la factura
        obj_ai = self.pool.get('account.invoice')
        ############################################################
        root = ''
        for id in ids:
            wh_brw = self.browse(cr, uid, id)

            period = wh_brw.period_id.name.split('/')
            period2 = period[0] + period[1]

            # Modificaciones para extraer la fecha final del periodo
            fecha_fin = datetime.datetime.strptime(wh_brw.period_id.date_stop,
                                                   '%Y-%m-%d')
            #######################################################

            root = Element("RelacionRetencionesISLR")
            root.attrib['Periodo'] = period2.strip()
            root.attrib['RifAgente'] = wh_brw.company_id.partner_id.vat[2:]

            sql = '''SELECT partner_vat, control_number, porcent_rete,
            concept_code, invoice_number, SUM(COALESCE(base, 0)) as base,
            account_invoice_id
            FROM islr_xml_wh_line
            WHERE period_id = %s
            GROUP BY partner_vat, control_number, porcent_rete, concept_code,
            invoice_number, account_invoice_id''' % (wh_brw.period_id.id)
            cr.execute(sql)
            xml_lines = cr.fetchall()
            if wh_brw.xml_ids:
                for line in xml_lines:
                    partner_vat, control_number, porcent_rete, concept_code, \
                        invoice_number, base, inv_id = line
                    fecha_contable_ai = datetime.datetime.strptime(obj_ai.browse(cr, uid, inv_id).date_invoice, "%Y-%m-%d").strftime("%d/%m/%Y")
                    detalle = SubElement(root, "DetalleRetencion")
                    inv_num = invoice_number.replace("-", "")
                    con_num = control_number.replace("-", "").replace("/", "")
                    SubElement(detalle, "RifRetenido").text = partner_vat
                    SubElement(detalle, "NumeroFactura").text = inv_num
                    SubElement(detalle, "NumeroControl").text = con_num
                    SubElement(detalle, "FechaOperacion").text = \
                        fecha_contable_ai
                    SubElement(detalle, "CodigoConcepto").text = concept_code
                    SubElement(detalle, "MontoOperacion").text = str(base)
                    SubElement(detalle, "PorcentajeRetencion").text = \
                        str(porcent_rete)

            # XML payroll
            for line_payroll in wh_brw.xml_payroll_ids:
                detalle = SubElement(root, "DetalleRetencion")
                SubElement(detalle, "RifRetenido").text = \
                    line_payroll.partner_vat
                SubElement(detalle, "NumeroFactura").text = str(0)
                SubElement(detalle, "NumeroControl").text = str(0)
                SubElement(detalle, "FechaOperacion").text = \
                    fecha_fin.strftime('%d/%m/%Y')
                SubElement(detalle, "CodigoConcepto").text = '001'
                SubElement(detalle, "MontoOperacion").text = \
                    str(line_payroll.total_amount)
                SubElement(detalle, "PorcentajeRetencion").text = \
                    str(line_payroll.withholding)

        self.indent(root)

        return tostring(root, encoding="ISO-8859-1")
islr_xml_wh_doc()
