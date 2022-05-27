from odoo import fields, models
from functools import partial
from odoo.tools.misc import formatLang


class SaleOrder(models.Model):
    _inherit = "sale.order"

    customer_age = fields.Integer(string="Customer age")


    def get_attachments(self):
        for sale in self:
            print(f"\n\n-------id----{sale.id}------\n\n")
            if sale.partner_id:
                attachments = self.env['ir.attachment'].search([
                    ('res_model', '=', 'sale.order'), ('res_id', '=', sale.id)
                ])

            for a in attachments:
                print('\n\n-----a-----\n\n', a.id)

            att = self.env['ir.attachment'].search([('res_model', '=', 'account.move'),('res_id', '=', 22)])
            print(f"\n\n\n\n\n ---------att----{att}--\n\n\n\n\n")
            # for n in att:
            #     print(f'\n\n-----invoice nu attachments-- {n}---\n\n')
            return attachments



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    def _prepare_invoice_line(self):
        invoice_vals = super(SaleOrderLine, self)._prepare_invoice_line()
        for sale in self:
            if sale.product_id:
                attachments = self.env['ir.attachment'].search([
                    ('res_model', '=', 'sale.order'), ('res_id', '=', sale.id)
                ])

        print('\n\n----attch------\n\n', attachments)
        for a in attachments:
                print('\n\n-----a-----\n\n', a.id)

        # att = self.env['account.move'].create({
        #     'attachment_ids': [(0, 0, attachments.ids)]
        # })
        print('\n\n-----------Invoice vals--------\n\n', invoice_vals)
        return invoice_vals
