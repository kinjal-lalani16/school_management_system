from odoo import fields, models


class Test(models.Model):

    _name = "test.test"
    _rec_name = "test_name"
    _description = 'test details'
    _inherits = {'profesor.record': 'profesor_id'}

    test_name = fields.Char(string="Test Name", required=True)
    test_date = fields.Char(string="Date")
    profesor_id = fields.Many2one(
        'profesor.record', string="Professor", required=True)
