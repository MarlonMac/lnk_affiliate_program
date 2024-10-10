from odoo import models, fields

class CommissionProgram(models.Model):
    _name = 'affiliate.program'
    _description = 'Programa de Comisión'

    name = fields.Char(string="Nombre del Programa", required=True)
    company_id = fields.Many2one('res.company', string="Compañía")
    tipo_comision = fields.Selection([
        ('fijo', 'Monto Fijo'),
        ('porcentaje', 'Porcentaje de Venta')], 
        string="Tipo de Comisión", default='porcentaje')
    valor_comision = fields.Float(string="Valor de la Comisión")
    descripcion = fields.Text(string="Descripción")