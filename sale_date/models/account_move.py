from odoo import api, fields, models


class Account(models.Model):
    _inherit = "account.move"

    cubes_date = fields.Date(string="Sales Force Date")