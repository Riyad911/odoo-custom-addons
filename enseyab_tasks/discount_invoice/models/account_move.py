from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    discount = fields.Float(
        string="الخصم % ",
        default=0.0,
        digits=(5, 2),
    )

    @api.onchange('discount')
    def _onchange_discount(self):
        for record in self:
            for line in record.invoice_line_ids:
                line.discount = record.discount
