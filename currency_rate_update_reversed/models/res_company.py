from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    currency_rates_autoupdate = fields.Boolean(
        string='Automatic Currency Rates (OCA)',
        default=True,
        help='Enable regular automatic currency rates updates',
        oldname='auto_currency_up',
    )
