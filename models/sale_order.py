from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    es_venta_afiliado = fields.Boolean(string="Venta de Afiliado")
    affiliate_id = fields.Many2one('affiliate.affiliate', string="Afiliado")