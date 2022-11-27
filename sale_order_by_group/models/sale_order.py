from odoo import api, fields, models


class Employee(models.Model):
    _inherit = "sale.order"

    branch_id = fields.Many2one('sale.order.branch',string='الفرع')


