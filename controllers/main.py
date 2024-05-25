from odoo import http
from odoo.http import request


class BkashController(http.Controller):
    _return_url = '/payment/bkash/return'
    _webhook_url = '/payment/bkash/webhook'

    @http.route(_return_url, type='http', auth='public', csrf=False, website=True)
    def bkash_return(self, **kwargs):
        # Extract data from the form
        payment_transaction = request.env['payment.transaction'].sudo().search(
            [('reference', '=', kwargs.get('paymentID'))])
        if payment_transaction:
            # Validate and confirm the payment
            # Update the payment_transaction status accordingly
            return request.redirect('/payment/process')
        return request.redirect('/shop')
