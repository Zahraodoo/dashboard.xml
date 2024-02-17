
# -*- coding: utf-8 -*-


from odoo import api, fields, models, _

from odoo.exceptions import ValidationError
import datetime

class FormationMode(models.Model):
    _name = 'formation.mode'



    name = fields.Char(string='Mode de Formation')
    # formation_ids = fields.One2many('formation.formation', 'modeformation_id', string='Formations avec ce mode')


