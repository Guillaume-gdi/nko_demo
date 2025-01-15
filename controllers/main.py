from odoo import http
from odoo.http import request


class NkoDemoController(http.Controller):

    @http.route('/nko_demo/pause_sub/<int:sale_order_id>', type='json', auth='public', website=True)
    def set_sale_order_state(self, sale_order_id):
        sale_order = request.env['sale.order'].sudo().browse(sale_order_id)
        if sale_order.exists():
            # TODO check that the user is the owner of the sale order ?
            sale_order.subscription_state = '4_paused'
            return {'status': 'success', 'message': 'State updated successfully'}
        else:
            return {'status': 'error', 'message': 'Sale order not found'}