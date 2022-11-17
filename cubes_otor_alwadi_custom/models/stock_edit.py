# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockQaunt(models.Model):
    _inherit = 'stock.quant'

    company_id = fields.Many2one(related='location_id.company_id', string='Company', store=True, readonly=False)


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    company_id = fields.Many2one(
        'res.company', 'Company', default=lambda self: self.env.company,
        index=True, readonly=False, required=True,
        help='The company is automatically set from your user preferences.')