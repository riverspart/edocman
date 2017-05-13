# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    thmdocument_time_mode_id = fields.Many2one('product.uom', string='Thmdocument Time Unit',
        help="This will set the unit of measure used in thmdocuments and tasks.\n"
             "If you use the timesheet linked to thmdocuments, don't "
             "forget to setup the right unit of measure in your employees.")
