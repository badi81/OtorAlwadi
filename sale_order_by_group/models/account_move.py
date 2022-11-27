from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    branch_id = fields.Many2one('sale.order.branch',compute="get_branch_id", store=True, string="الفرع")
    compute_branch = fields.Boolean(compute='get_compute_branch',store=False)


    def get_compute_branch(self):
        for elem in self:
            if not elem.branch_id:
                elem.sudo().get_branch_id()
            elem.compute_branch = False

    def get_branch_id(self):
        for elem in self:
            elem.branch_id=False
            sale_orders = self.env['sale.order'].search([('invoice_ids','!=',False)])
            for ele in sale_orders:
                if elem.id == ele.invoice_ids[0].id:
                    if not elem.branch_id:
                        elem.branch_id = ele.branch_id

