# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
import requests


_log = logging.getLogger(__name__)

URL = ""
# class odoo_exam_prixz(models.Model):
#     _name = 'odoo_exam_prixz.odoo_exam_prixz'
#     _description = 'odoo_exam_prixz.odoo_exam_prixz'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class SaleOrderExam(models.Model):
    _inherit = "sale.order"

    customer_vat = fields.Char(string="RFC cliente", compute="_compute_customer_vat", store=False)

    @api.onchange("partner_id")
    def _compute_customer_vat(self):
        if self.partner_id and self.partner_id.vat:
            self.customer_vat = self.partner_id.vat
        elif self.partner_id and not self.partner_id.var:
            self.customer_vat = "XAXX010101000"
        else: 
            self.customer_vat = ""


class StockPickingExam(models.Model):
    _inherit ="stock.picking"

    total_reservado = fields.Float(string="Total", compute="_compute_total_reservado", store=False)

    def _compute_total_reservado(self):

        total_reservado = sum(self.move_ids_without_package.mapped('forecast_availability'))
        self.total_reservado = total_reservado

    def fetch_urldata(self): 
        _log.info(" RECIBIENDO PRODUCTOS DEL GET")
        try:
            result = requests.get(URL)
            _log.info(" Resultado... %s" % result)
        except:
            _log.info("error")
