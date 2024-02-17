# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import re

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression


from odoo.tools import float_compare, float_round


class StockCategorie(models.Model):
    _name = "stock.categorie"
    _description = "Categorie"



    name = fields.Char('Name', required=True)
    description = fields.Html('Description', translate=True)
    stock_actuel = fields.Integer(string="Stock Actuel", compute="_compute_item_count")
    produits = fields.One2many('stock.produits','id_categorie', string="Produits")

    def _stock_actuel(self):
        for cat in self:
            # Pricelist item count counts the rules applicable on current template or on its variants.
            cat.stock_actuel = cat.env['stock.produits'].search_count([('id_categorie', '=', cat.id)])
