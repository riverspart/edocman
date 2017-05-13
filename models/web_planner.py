# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models


class PlannerThmdocument(models.Model):

    _inherit = 'web.planner'

    def _get_planner_application(self):
        planner = super(PlannerThmdocument, self)._get_planner_application()
        planner.append(['planner_thmdocument', 'Thmdocument Planner'])
        return planner

    def _prepare_planner_thmdocument_data(self):
        return {
            'timesheet_menu': self.env.ref('hr_timesheet_sheet.menu_act_hr_timesheet_sheet_form_my_current', raise_if_not_found=False),
        }
