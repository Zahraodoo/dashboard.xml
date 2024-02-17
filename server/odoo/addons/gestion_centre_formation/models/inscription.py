
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


class FormationInscription(models.Model):
    _name = 'formation.inscription'
    TYPE_SELECTION = [
        ('individuelle', 'Individuelle'),
        ('entreprise', 'Entreprise'),
    ]
    name = fields.Char(string='Nom de l\'apprenant', compute='_compute_apprenant_name', store=True)

    @api.depends('apprenant_id')
    def _compute_apprenant_name(self):
        for inscription in self:
            if inscription.apprenant_id:
                inscription.name = f" {'Inscription de:   '}{inscription.apprenant_id.name}"
            else:
                inscription.name = ""
    date_inscription = fields.Date(string='Date d\'inscription', default=fields.Date.today())
    formation_id = fields.Many2one('formation.formation', string='Formation', required=True)

    type_inscription = fields.Selection(TYPE_SELECTION, string='Type d\'inscription', default='individuelle')
    apprenant_id = fields.Many2one('formation.apprenants', string='Apprenant', required=True)
    entreprise_id = fields.Many2one('formation.entreprise', string='Entreprise')