# from exception import UserError

from odoo import fields, models


class DateWizard(models.TransientModel):

    _name = 'date.wizard'

    start_date = fields.Datetime(string="Start date")
    end_date = fields.Datetime(string="End date")

    def action_done(self):
        data = {
            'model': 'date.wizard',
            'form': self.read()[0]
        }
        order_details = self.env['sale.order'].search([
            ('date_order', '>=', self.start_date),
            ('date_order', '<=', self.end_date)])
        order_list = []
        date_list = []
        date_list.append(data['form'])
        data['date'] = date_list
        for i in order_details:
            order = {
                'name': i.name,
                'date_order': i.date_order,
                'expected_date': i.expected_date,
                'partner_id': i.partner_id.name,
                'user_id': i.user_id.name,
                'company_id': i.company_id.name,
                'amount_total': i.amount_total,
                'invoice_status': i.invoice_status
            }
            order_list.append(order)
        data['kinjal'] = order_list
        return self.env.ref(
            'school_management.order_sale_report').report_action(
            self, data=data)
