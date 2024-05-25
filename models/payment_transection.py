from odoo import _, api, fields, models


class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    bkash_type = fields.Char(string="bkash Transaction Type")

    def _get_specific_rendering_values(self, processing_values):
        """ Override of payment to return bkash-specific rendering values.

        Note: self.ensure_one() from `_get_processing_values`

        :param dict processing_values: The generic and specific processing values of the transaction
        :return: The dict of provider-specific processing values
        :rtype: dict
        """
        res = super()._get_specific_rendering_values(processing_values)
        if self.provider_code != 'bkash':
            return res
        return {
            'api_url': self.provider_id.bkash_request_payment(self.amount, self.reference),
        }