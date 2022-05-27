from odoo import fields, models

class Apartment(models.Model):
    _name = 'apartment.apartment'

    building_id = fields.Many2one('buildig.building', string='Building')

# class Building(models.Model):
#     _name = 'building.building'

#     apartment_ids = fields.One2many('apartment.apartment', 'building_id', string='Apartments')
#     project_ids = fields.Many2one('project.project', 'project_table',
#                   'project_id', 'project_name', string="projects")


class hr(models.Model):
    _inherit = 'hr.employee'

    hello = fields.Char(string='heello')
