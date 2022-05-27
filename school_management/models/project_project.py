from datetime import datetime

from odoo import api, fields, models

from dateutil.relativedelta import relativedelta

from odoo.exceptions import ValidationError


class ProjectProject(models.Model):

    """docstring for ProjectProject"models.Model def __init__(self, arg):
        super(ProjectProject,models.Model.__init__()
        self.arg = arg"""

    _inherit = 'project.project'

    end_day = fields.Datetime(string='End date')
    number_of_days = fields.Integer(
        string='Number of Days', store=True)

    # @api.depends('create_date', 'end_day')
    # def calculate_number_of_day(self):

    #     """ This method will giv difference between create_date and
    #     end_date..!"""
    #     if self.create_date > self.end_day:
    #         raise ValidationError('End date should be bigger than create_date')
    #     if not self.create_date:
    #         self.create_date = datetime.today()
    #         result = relativedelta(self.end_day, self.create_date)
    #         self.number_of_days = int(result.days)
    #     else:
    #         result = relativedelta(self.end_day, self.create_date)
    #         self.number_of_days = int(result.days)
