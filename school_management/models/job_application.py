from odoo import fields, models


class JobApplication(models.Model):

    _name = 'job.application'
    _description = 'jon application'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email Address')
    phone = fields.Char(string='Phone No')
    designation_id = fields.Many2one('job.designation', string="Designation")
