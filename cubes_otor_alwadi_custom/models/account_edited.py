# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError



class AccountAccount(models.Model):
    _inherit = 'account.account'

    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=False,
                                 default=lambda self: self.env.company)


class AccountMove(models.Model):
    _inherit = 'account.move'

    company_id = fields.Many2one(comodel_name='res.company', string='Company',
                                 store=True, readonly=False,
                                 compute='_compute_company_id')


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    company_id = fields.Many2one(related='move_id.company_id', store=True, readonly=False)