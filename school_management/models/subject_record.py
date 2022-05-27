from datetime import datetime, timedelta

from odoo import fields, models


class SubjectRecord(models.Model):

    _name = "subject.record"
    _rec_name = "subject_name"
    _description = 'subject details'

    subject_name = fields.Char(sting="Name", required=True)
    subject_details = fields.Char(string="Details")
    profesor_ids = fields.One2many(
        'profesor.record', 'subject_id', string='Profesor')
    profesor_count = fields.Integer(compute='get_profesor_count')
    start_date = fields.Date(
        string='Last modified', default=datetime.today(), required=True)
    sale_id = fields.Many2one('sale.order', string='Sale Id')
    product_id = fields.Many2one('product.product', string='Product Id')

    def get_profesor(self):
        return {
            'name': 'Professor',
            'domain': [('subject_id', '=', self.id)],
            'context': {'default_subject_id': self.id},
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'profesor.record',
            'view_mode': 'tree,form',
            'view_id': False,
        }

    # function to get profesor count for subject
    def get_profesor_count(self):
        count = self.env['profesor.record'].search_count([
            ('subject_id', '=', self.id)])
        self.profesor_count = count

    def create_profesor(self):
        self.ensure_one()
        form_view = self.env.ref(
            'school_management.profesor_record_form_view_base')
        data = {
            'name': 'Create Profesor',
            'type': 'ir.actions.act_window',
            'res_model': 'profesor.record',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'target': 'new',
            'views': [(form_view.id, 'form')],
            'view_id': form_view.id,
            'flags': {'action_buttons': True},
            'context': {'default_subject_id': self.id, }
        }
        return data

    def _scheduler_demo(self):
        subject_record = self.env['subject.record'].search([])
        for i in subject_record:
            i.write({
                'start_date': i.start_date + timedelta(days=1)
            })

    # def send_email(self):
    #     self.ensure_one()
    #     ir_model_data = self.env['ir.model.data']
    #     try:
    #         template_id = ir_model_data.get_object_reference(
    #             'school_management.email_record_template')[1]
    #     except ValueError:
    #         template_id = False
    #     try:
    #         compose_form_id = ir_model_data.get_object_reference(
    #             'mail', 'email_compose_message_wizard_form')[1]
    #     except ValueError:
    #         compose_form_id = False
    #     ctx = {
    #         'default_model': 'subject.record',
    #         'default_res_id': self.ids[0],
    #         'default_use_template': bool(template_id),
    #         'default_template_id': template_id,
    #         'default_composition_mode': 'comment',
    #     }
    #     return {
    #         'name': ('Compose Email'),
    #         'type': 'ir.actions.act_window',
    #         'view_mode': 'form',
    #         'res_model': 'mail.compose.message',
    #         'views': [(compose_form_id, 'form')],
    #         'view_id': compose_form_id,
    #         'target': 'new',
    #         'context': ctx,
    #     }
