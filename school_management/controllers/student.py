from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager

class Student(CustomerPortal):

    def _prepare_home_portal_values(self):
        values = super(Student, self)._prepare_home_portal_values()
        student_count = request.env['student.record'].search_count([])
        values['student_count'] = student_count

        return values

    @http.route(['/my/student', '/my/student/page/<int:page>'], auth="user", website=True, type="http")

    def student_details(self, page=1, sortby=None, **kw):
        values = self._prepare_portal_layout_values()
        students = request.env['student.record'].search([])
        searchbar_sortings = {
            'date': {'label': ('Newest'), 'order': 'create_date desc'},
            'name': {'label': ('Name'), 'order': 'student_id'},
        }
        student_count = students.search_count([])
        if not sortby:
            sortby = 'date'
        order = searchbar_sortings[sortby]['order']
        pager = portal_pager(
            url="/my/student",
            total=student_count,
            page=page,
            step=2
        )
        student = students.search([], order=order, limit=2, offset=pager['offset'])
        values.update({
            'student': student,
            'page_name': 'student',
            'default_url': '/my/student',
            'pager': pager,
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby
        })

        return request.render("school_management.portal_students", values)
