from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Adding a custom field
    x_custom_discount_reason = fields.Char(string='Discount Reason')
    
    # Custom state checking logic
    @api.onchange('partner_id')
    def _onchange_partner_id_custom(self):
        if self.partner_id and self.partner_id.credit_limit < 0:
            return {
                'warning': {
                    'title': 'Credit Limit Warning',
                    'message': 'This customer has reached their credit limit!',
                }
            }

    # Senior Logic: Overriding write
    def write(self, vals):
        if 'state' in vals and vals['state'] == 'sale':
            # Add custom professional logic when order is confirmed
            self._message_log(body="Order confirmed by Senior Automation System.")
        return super(SaleOrder, self).write(vals)
