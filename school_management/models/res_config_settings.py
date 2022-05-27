from odoo import api, fields, models


class ResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'

    condition = fields.Boolean(string='Condition')
    team_condition = fields.Char(string='Team condition')
    student_id = fields.Many2one('student.record', string='Student')

    # onchange method for condition
    @api.onchange('condition')
    def check_condition(self):
        if not self.condition:
            self.team_condition = False

    @api.model
    # get_values method to add field in res.config file
    def get_values(self):
        res = super(ResConfigSetting, self).get_values()
        icpsudo = self.env['ir.config_parameter'].sudo()
        sale_condtion = icpsudo.get_param('sale.condition')
        sale_team_condition = icpsudo.get_param('sale.team_condition')
        student_id = int(icpsudo.get_param('school_management.student_id'))
        if student_id and \
                not self.env['student.record'].browse(student_id).exists():
            student_id = False
        res.update(condition=sale_condtion,
                   team_condition=sale_team_condition,
                   student_id=student_id)
        return res

    # get_vakues method to set field in res.config file
    def set_values(self):
        super(ResConfigSetting, self).set_values()
        icpsudo = self.env['ir.config_parameter'].sudo()
        icpsudo.set_param("sale.condition", self.condition)
        icpsudo.set_param("sale.team_condition", self.team_condition)
        icpsudo.set_param("school_management.student_id", self.student_id.id)


    @api.model
    def set_button_parameters(self):
        settings = self.env['res.config.settings'].write({
            'auth_signup_uninvited': 'b2c',
        })
        settings.execute()
