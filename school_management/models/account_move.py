from odoo import api, models

from datetime import date, datetime
#from dateutil.relativedelta import relativedelta

class AccountMove(models.Model):

    _inherit = 'account.move'

    def action_send(self):
        template_id = self.env.ref('school_management.email_record_template').id
        self.env['mail.template'].browse(template_id).send_mail(
            self.id, force_send=True)
        ctx = {
            'default_model': 'account.move',
            'default_res_id': self.ids[0],
            'default_use_template': bool(template_id),
            'default_template_id': template_id,
           # 'default_composition_mode': 'comment',
            'mark_so_as_sent': True,
            'custom_layout': "mail.mail_notification_paynow",
           # 'invoice': self.env.context.get('invoice', False),
            'force_email': True,

        }
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            'context': ctx,
        }

    def invoice_reminder(self):
        invoice = self.env['account.move'].search([
            ('type', '=', 'out_invoice'),
            ('state', '=', 'posted'),
            ('amount_residual', '>', 0)])

        for records in invoice:
            if records.invoice_date_due:
                current_date = date.today()
                diff = (records.invoice_date_due - current_date).days
                if diff == 2:
                    records.action_send()


    @api.model_create_multi
    def create(self, vals_list):
        moves = super(AccountMove, self).create(vals_list)
        print('\n\nvals---------->', vals_list)
        for move in moves:
            sale = move.line_ids.mapped('sale_line_ids.order_id')
            print('\n\nsale--------------->', sale)
            print('\n\nmodel--------------->', self._name)
            if not sale:
                continue
            for attachment in self.env['ir.attachment'].search(
                [('res_model', '=', 'sale.order'),
                 ('res_id', '=', sale.id)]):
                attachment.copy({'res_model': self._name, 'res_id': move.id})
        return moves
