from odoo import fields, models

class JobDesignation(models.Model):

    _name = 'job.designation'
    _description = 'job designation'

    name = fields.Char(string='Job name', required=True)
    application_ids = fields.One2many('job.application', 'designation_id',
        string="Application")
