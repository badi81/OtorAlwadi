# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.osv import expression



class SaleReportEdited(models.Model):
    _inherit = "sale.report"

    branch_id = fields.Many2one('sale.order.branch', string='الفرع', readonly=True)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):

        fields['branch_id '] = ", s.branch_id as branch_id"
        groupby += ', s.branch_id'

        return super(SaleReportEdited, self)._query(with_clause, fields, groupby, from_clause)


