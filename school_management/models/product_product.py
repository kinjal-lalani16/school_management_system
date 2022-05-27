from odoo import api, fields, models


class ProductProduct(models.Model):

    _inherit = "product.product"

    product_short_name = fields.Char(string="Product Short Name")
    product_description = fields.Char(string="Product Description")
    tex = fields.Float(string="tex")
    actual_price = fields.Float(string="Actual Price")
    product_detail = fields.Char(string="Product Details")
    product_ref = fields.Char('product ref')

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        product = []
        if self._context.get('sale_id'):
            sale_rec = self.env['sale.order'].browse(
                self._context.get('sale_id'))
            product = [i.product_id.id for i in sale_rec.order_line]
            product_rec = self.search([('id', 'in', product)]).name_get()
            return product_rec
        else:
            return super(ProductProduct, self).name_search(
                name, args, operator, limit)
