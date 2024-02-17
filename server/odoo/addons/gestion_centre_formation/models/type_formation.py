
# -*- coding: utf-8 -*-


from odoo import api, fields, models, _

from odoo.exceptions import ValidationError
import datetime

class FormationType(models.Model):
    _name = 'formation.type'



    name = fields.Char(string='Type de formation')
    # formation_ids = fields.One2many('formation.formation', 'typeformation_id', string='Formations de ce Type')


