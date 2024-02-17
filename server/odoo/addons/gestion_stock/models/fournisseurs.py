# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import re

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression


from odoo.tools import float_compare, float_round


class StockFournisseurs(models.Model):
    _name = "stock.fournisseurs"
    _description = "Fournisseurs"



    name = fields.Char('Name', index=True, required=True)
    contact  = fields.Char('Contact')
    adresse = fields.Char('Adresse')
