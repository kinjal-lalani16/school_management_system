import json
from odoo import http
from odoo.http import request
from odoo.addons.website_form.controllers.main import WebsiteForm


class WbsiteFormJob(WebsiteForm):

    @http.route('/create_job_application/<string:model_name>', type='http', auth="public", methods=['POST'], website=True)
    def website_form_job(self, model_name, **kwargs):
        job = request.env['job.application'].sudo().create(kwargs)
        return json.dumps({'id': job.id})
