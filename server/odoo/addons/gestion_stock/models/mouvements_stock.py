# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import re

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression


from odoo.tools import float_compare, float_round


class StockMouvements(models.Model):
    _name = "stock.mouvements"
    _description = "Mouvement"


    name = fields.Char(string='Reference Mouvement')
    quantite_mouvement = fields.Integer(string='Quantite Mouvement')
    date = fields.Date('Date Mouvement', help="Date for this Mouvement")
    id_produit = fields.Many2one('stock.produits', required=True, string='Produit')
    type_mouvement = fields.Selection([
            ('vente', 'Vente'),
            ('achat', 'achat'),
        ],string='Type de Movement',default='vente')

