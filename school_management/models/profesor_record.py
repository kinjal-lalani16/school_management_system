import re

from datetime import date

from dateutil.relativedelta import relativedelta

from odoo import api, fields, models

from odoo.exceptions import ValidationError


class ProfesorRecord(models.Model):

    _name = "profesor.record"
    _rec_name = "profesor_id"
    _description = "profesor"

    profesor_id = fields.Many2one('res.partner', string="Professor Name", required=True)
    profesor_department = fields.Char(string="Department", required=True)
    profesor_dob = fields.Date(string="Date of Birth", required=True)
    profesor_phone_number = fields.Char(string="Phone Number")
    profesor_age = fields.Integer(string="Age", compute='get_dob', store=True)
    profesor_email = fields.Char(string="E-mail")
    profesor_gender = fields.Selection(
        [('m', 'Male'), ('f', 'Female'), ('o', 'Other')], string='Gender')
    profesor_blood_group = fields.Selection([('A+', 'A+ve'), ('B+', 'B+ve'), (
        'O+', 'O+ve'), ('AB+', 'AB+ve'), ('A-', 'A-ve'), ('B-', 'B-ve'), (
        'O-', 'O-ve'), ('AB-', 'AB-ve')], string='Blood Group')
    subject_id = fields.Many2one('subject.record', string="Subject")
    subject_description = fields.Char(related="subject_id.subject_details",
                                      readonly=True)
    student_ids = fields.One2many(
        'student.record', 'profesor_id', string="Student")

    # Name get method to get phone number with profesor name.
    @api.model
    def name_get(self):
        profesor_list = []
        for i in self:
            if self._context.get('profesor_id'):
                name = i.profesor_phone_number + ' ' + i.profesor_id.name
                profesor_list.append((i.id, name))
        return profesor_list

    # onchange function to get age through entered dob

    @api.depends('profesor_dob')
    def get_dob(self):
        for record in self:
            if record.profesor_dob:
                date_record = record.profesor_dob
                current_date = date.today()
                result = relativedelta(current_date, date_record)
                age = int(result.years)
                self.profesor_age = age

    # constraint to input valid mobile number
    @api.constrains('profesor_phone_number')
    def check_number(self):
        if self.profesor_phone_number:
            match = re.match(r'[789]\d{9}$', self.profesor_phone_number)
            if match is None:
                raise ValidationError('Not a valid mobile number')

    # constrain for not allowing user to enter current date or future date
    @api.constrains('profesor_dob')
    def validate_dob(self):
        if self.profesor_dob >= (date.today()):
            raise ValidationError("Date you have enter is not valid..!")

    @api.constrains('profesor_age')
    def check_age(self):
        if self.profesor_age < 25:
            raise ValidationError(
                'Can not ragister as a professor.Age must be above 25.!')

    @api.constrains('profesor_email')
    def validate_mail(self):
        if self.profesor_email:
            match = re.match('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',
                             self.profesor_email)
            if match is None:
                raise ValidationError('Not a valid E-mail ID')

    def create_student(self):
        student_record = self.env['student.record'].search([])
        email_list = []
        for i in student_record:
            email_list.append(i.student_email)
        student = self.env['student.record'].create({
            'student_id': 'Kinjal',
            'last_name': 'Lalani',
            'student_dob': '2005-12-10',
            'student_email': 'kinjal123@gmail.com'
        })
        pop_up = {
            'name': 'Message',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'msg.wizard',
            'target': 'new',
            'context': {'default_name': "Student created successfully."}
        }
        for i in student:
            for j in email_list:
                if j == i.student_email:
                    raise ValidationError(
                        'Email alredy exist..!You can not create student with \
                        this email..!')
            else:
                return pop_up
