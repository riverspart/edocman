# -*- coding: utf-8 -*-
from odoo import models, fields, api

from odoo.exceptions import UserError, ValidationError
#Import logger
import logging
#Get the logger
_logger = logging.getLogger(__name__)

#External import
import datetime

class thmdocument_file(models.Model):
    _name = 'thmdocument.file'
    name = fields.Char(required=True)
    code = fields.Char(string='Code', required=True, index=True, default='/HS')
    date_start = fields.Date(string='Start', index=True, copy=False)
    date_deadline = fields.Date(string='Deadline', index=True, copy=False)
    description = fields.Html(string='Description')
    thmdocument_task_ids = fields.Many2many('thmdocument.task', 'thmdocument_file_task_rel', 'file_id',
                                       'thmdocument_task_id', string='Task')
    create_date = fields.Datetime(index=True , copy=False, readonly=True)
    create_uid = fields.Many2one('res.users',
                                 string='Nguoi tao',
                                 default=lambda self: self.env.uid,
                                 index=True, track_visibility='always', readonly=True)