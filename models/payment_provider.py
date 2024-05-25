import requests
from odoo import api, fields, models, _

from odoo.addons.payment_aps import const


class PaymentProviderBkash(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(
        selection_add=[('bkash', 'bKash')], ondelete={'bkash': 'set default'}
    )
    # bKash credentials and endpoints
    bkash_base_url = fields.Char("bKash Base URL", required=True)
    bkash_api_key = fields.Char("bKash API Key", required=True)
    bkash_api_secret = fields.Char("bKash API Secret", required=True)

    @api.model
    def bkash_request_payment(self, amount, order_reference):
        """ Request a payment from bKash """
        # Simplified example of making a request to bKash (replace with actual implementation)
        response = requests.post(
            f"{self.bkash_base_url}/checkout/payment/create",
            json={
                "amount": amount,
                "reference": order_reference,
                "currency": "BDT",
                # other required fields
            },
            headers={
                "accept": "application/json",
                "content-type": "application/json"
                # "X-Api-Key": self.bkash_api_key,
                # "X-Api-Secret": self.bkash_api_secret,
            }
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"bKash API request failed: {response.text}")

    def _get_default_payment_method_codes(self):
        """ Override of `payment` to return the default payment method codes. """
        default_codes = super()._get_default_payment_method_codes()
        if self.code != 'bkash':
            return default_codes
        return const.DEFAULT_PAYMENT_METHODS_CODES

