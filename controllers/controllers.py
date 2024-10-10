from odoo import http
from odoo.http import request

class AffiliateController(http.Controller):

    @http.route(['/shop'], type='http', auth="public", website=True)
    def shop(self, **kw):
        affiliate_id = request.params.get('affiliate_id')
        # Aquí puedes realizar acciones con el ID del afiliado, 
        # como registrar la visita o la compra.
        return request.render("website_sale.products", {})