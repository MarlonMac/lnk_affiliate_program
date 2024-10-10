from odoo import models, fields

class Affiliate(models.Model):
    _name = 'affiliate.affiliate'
    _description = 'Afiliado'

    name = fields.Char(string="Nombre", required=True)
    email = fields.Char(string="Correo Electrónico", required=True)
    company_id = fields.Many2one('res.company', string="Compañía")
    program_id = fields.Many2one('affiliate.program', string="Programa de Comisión")
    enlace_afiliado = fields.Char(string="Enlace de Afiliado", compute="_compute_enlace_afiliado")

    def _compute_enlace_afiliado(self):
        # Genera el enlace de afiliado aquí, por ejemplo:
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        for record in self:
            record.enlace_afiliado = f"{base_url}/shop?affiliate_id={record.id}"