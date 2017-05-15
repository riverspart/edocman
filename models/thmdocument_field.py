# -*- coding: utf-8 -*-
from odoo import models, fields, api

from odoo.exceptions import UserError, ValidationError
#Import logger
import logging
#Get the logger
_logger = logging.getLogger(__name__)

#External import
import datetime

class thmdocument_field(models.Model):
    _name = 'thmdocument.field'
    name = fields.Char(required=True)
    lastModified = fields.Date('Last updated')

