# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import re

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression


from odoo.tools import float_compare, float_round


class StockCommandes(models.Model):
    _name = "stock.commandes"
    _description = "Commandes"



    name = fields.Char('ID',  required=True)
    contact  = fields.Char('Contact')
    adresse = fields.Char('Adresse')
    id_fournisseur = fields.Many2one('stock.fournisseurs', required=True, string='Fournisseur')
    date = fields.Date('Date_Commande', help="Date for this Commande")
    date_livraison_prevue = fields.Date('Date_Livraison_Prevue', help="Date for this Commande")

    statut = fields.Selection([
        ('en_attente', 'en_attente'),
        ('en_cours', 'en_cours'),
        ('terminee', 'terminée'),
        ('annulee', 'annulée'),
    ], string='Statut de Commande')

