# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class Department(models.Model):

    _inherit = 'hr.department'

    code = fields.Char(string='Code', required=True, index=True, default='/TTr-CNTT')

