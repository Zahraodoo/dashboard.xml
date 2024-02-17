
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import base64
import hashlib
import io
import itertools
import logging
import mimetypes
import os
import re
import uuid

from collections import defaultdict
from PIL import Image
import PyPDF2

from odoo import api, fields, models, tools, _,SUPERUSER_ID
from odoo.exceptions import AccessError, ValidationError, MissingError, UserError
from odoo.tools import config, human_size, ustr, html_escape, ImageProcess, str2bool
from odoo.tools.mimetypes import guess_mimetype
from odoo.osv import expression


class FormationEnseignants(models.Model):
    _name = 'formation.enseignants'


    name = fields.Char('Name')
