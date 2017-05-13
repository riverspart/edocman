# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ThmdocumentConfiguration(models.TransientModel):
    _name = 'thmdocument.config.settings'
    _inherit = 'res.config.settings'

    company_id = fields.Many2one('res.company', string='Company', required=True,
        default=lambda self: self.env.user.company_id)
    thmdocument_time_mode_id = fields.Many2one(related='company_id.thmdocument_time_mode_id', string="Thmdocument Time Unit *")
    module_pad = fields.Selection([
        (0, "Task description is plain text"),
        (1, "Collaborative rich text on task description")
        ], string="Pads",
        help='Lets the company customize which Pad installation should be used to link to new pads '
             '(for example: http://ietherpad.com/).\n'
             '-This installs the module pad.')
    module_rating_thmdocument = fields.Selection([
        (0, "No customer rating"),
        (1, 'Track customer satisfaction on tasks')
        ], string="Rating on task",
        help="This allows customers to give rating on provided services")
    generate_thmdocument_alias = fields.Selection([
        (0, "Do not create an email alias automatically"),
        (1, "Automatically generate an email alias at the thmdocument creation")
        ], string="Thmdocument Alias",
        help="Odoo will generate an email alias at the thmdocument creation from thmdocument name.")
    module_thmdocument_forecast = fields.Boolean(string="Forecasts, planning and Gantt charts")

    @api.multi
    def set_default_generate_thmdocument_alias(self):
        check = self.env.user.has_group('base.group_system')
        Values = check and self.env['ir.values'].sudo() or self.env['ir.values']
        for config in self:
            Values.set_default('thmdocument.config.settings', 'generate_thmdocument_alias', config.generate_thmdocument_alias)
