# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import re

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression


from odoo.tools import float_compare, float_round


class StockDetailsCommande(models.Model):
    _name = "stock.details_commande"
    _description = "Détails_Commande"



    name = fields.Char('ID',  required=True)
    id_commande  = fields.Many2one('stock.commandes', required=True, string='Commande')
    date = fields.Date('Date_Commande', help="Date for this Commande")
    id_produit = fields.Many2one('stock.produits', required=True, string='Produit')

    quantite_commande = fields.Integer(string='Quantite_Commande')
    prix_unitaire_commande = fields.Float(string='Prix_Unitaire_Commande')


