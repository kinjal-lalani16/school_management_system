from odoo import fields, models


class MsgWizard(models.TransientModel):
    _name = "msg.wizard"

    name = fields.Char('Message')
