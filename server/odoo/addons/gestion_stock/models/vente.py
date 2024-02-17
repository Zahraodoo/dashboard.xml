# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import re

from odoo import api, fields, models, tools, _



class StockVentes(models.Model):
    _name = "stock.vente"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Integer(string="Numéro Vente", default=0, compute='incrementer_numero_versement', store=True)

    @api.depends('id_produit')
    def incrementer_numero_versement(self):
        for record in self:
            dernier_paiement = self.env['stock.vente'].search(
                [('id_produit', '=', record.id_produit.id)],
                order='id desc', limit=1)
            print('dernier_paiement')
            dernier_numero = dernier_paiement.name + 1 if dernier_paiement else 0
            record.name = dernier_numero
    client = fields.Char(string='Nom/Prenom Client')
    contacte_client = fields.Char(string='Télephone Client')
    num_client = fields.Char(string='Numéro d"identiter Client')
    quantite_vente = fields.Integer(string='Quantite Vendue')
    prix_unitaire = fields.Float(string='Prix Unitaire Vente',related='id_produit.prix_vente')
    categorie_produit = fields.Many2one('stock.categorie',related='id_produit.id_categorie', string='Ctegorie Produit')

    #, related = 'id_produit.id_categorie'
    prix_totale = fields.Float(string='Prix Totale Vente', tracking=True ,compute='compute_prix_totale', store=True)

    @api.depends('prix_unitaire', 'quantite_vente')
    def compute_prix_totale(self):
        for record in self:
            if record.prix_unitaire != 0.0:
                totale = (record.prix_unitaire) * (record.quantite_vente)
                record.prix_totale = totale
            else:
                record.prix_totale = 0.0
    date_vente = fields.Date('Date Vente', help="Date for this Mouvement", required=True)
    id_produit = fields.Many2one('stock.produits', required=True, string='Produit')
    default_code = fields.Char('Référence interne',related='id_produit.default_code')
    barcode = fields.Char('Code-barres', copy=False,related='id_produit.barcode')
    code_qr = fields.Char('Code-QR', copy=False,related='id_produit.code_qr')
    user_id = fields.Many2one('res.users', string='Vendeur', required=False, default=lambda self: self.env.user, redonly=True)
    remarque = fields.Html('Remarques', translate=True, help="pour des informations supplémentaires sur la vente, si nécessaire")
    currency_id = fields.Char(String='Currency', default='DA')

    @api.model
    def create(self, values):
        sale = super(StockVentes, self).create(values)
        sale.id_produit.sale_quantity += sale.quantite_vente
        return sale

    def write(self, values):
        super(StockVentes, self).write(values)
        self.id_produit.sale_quantity = sum(self.mapped('quantite_vente'))
        return True
