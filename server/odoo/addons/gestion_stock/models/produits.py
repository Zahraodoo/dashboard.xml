# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
import re

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError
from odoo.osv import expression


from odoo.tools import float_compare, float_round



class StockProduits(models.Model):
    _name = "stock.produits"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    code = fields.Char(string='Reference')
    priority = fields.Selection([
        ('0', 'Normal'),
        ('1', 'Favorite'),
    ], default='0', string="Favorite")
    name = fields.Char('Name', index=True, required=True)
    description = fields.Html('Description et Caractiristiques ', translate=True)
    prix_vente = fields.Float(string='Prix de vente')
    prix_achat = fields.Float(string="Prix d'achat")

    default_code = fields.Char('Référence interne')
    barcode = fields.Char(
        'Code-barres', copy=False,
        help="International Article Number used for product identification.")
    code_qr = fields.Char(
        'Code-QR', copy=False)

    id_categorie = fields.Many2one('stock.categorie', required=True, string='Ctegorie Produit')
    image_variant_1920 = fields.Image("Image Produit", max_width=1920, max_height=1920)
    stock_actuel = fields.Integer(string="Stock Actuel")
    seuil_minimum = fields.Integer(string='Quantité minimale',help="quantité minimale avant de déclencher une alerte de réapprovisionnement.")
    vente_ids = fields.One2many('stock.vente','id_produit',string='les ventes de produit', domain = "[('id_produit', '=',id )]")
    achat_ids = fields.One2many('stock.achat','id_produit',string='les achat de produit', domain = "[('id_produit', '=',id )]")
    active = fields.Boolean('Active', default=True, help="If unchecked, it will allow you to hide the product without removing it.")
    currency_id = fields.Char(String='Currency', default='DA')
    def open_pricelist_rules(self):
        self.ensure_one()
        domain = ['|',('id_produit', 'in', self.vente_ids.ids)]
        return {
            'name': _('Price Rules'),
            'view_mode': 'tree,form',
            # 'views': [(self.env.ref('gestion_stock.product_pricelist_item_tree_view_from_product').id, 'tree'), (False, 'form')],
            'res_model': 'gestion_stock.stock.vente',
            'type': 'ir.actions.act_window',
            'target': 'current',
            'domain': domain,
            'context': {
                # 'default_product_tmpl_id': self.id,
                # 'default_applied_on': '1_product',
                # 'product_without_variants': self.product_variant_count == 1,
            },
        }
    def action_open_label_layout(self):
        action = self.env['ir.actions.act_window']._for_xml_id('gestion_stock.action_open_label_layout')
        action['context'] = {'default_vente_ids': self.ids}
        return action

    pricelist_item_count = fields.Integer("Nombre de vente", compute="_compute_item_count", store=True)
    achat_item_count = fields.Integer("Nombre de Achat", compute="_compute_item_count_achat", store=True)

    @api.depends('vente_ids')
    def _compute_item_count(self):
        for produit in self:
            # Pricelist item count counts the rules applicable on current template or on its variants.
            #produit.pricelist_item_count = produit.env['stock.vente'].search_count([('id_produit', '=', produit.id)])
            vente_records = produit.env['stock.vente'].search([('id_produit', '=', produit.id)])
            total_quantity_sold = sum(vente_record.quantite_vente for vente_record in vente_records)
            produit.pricelist_item_count = total_quantity_sold

    @api.depends('achat_ids')
    def _compute_item_count_achat (self):
        for produit in self:
            # Pricelist item count counts the rules applicable on current template or on its variants.
            #produit.pricelist_item_count = produit.env['stock.vente'].search_count([('id_produit', '=', produit.id)])
            achat_records = produit.env['stock.achat'].search([('id_produit', '=', produit.id)])
            total_quantity_sold = sum(achat_records.quantite_acheter for achat_records in achat_records)
            produit.achat_item_count = total_quantity_sold

    # def _compute_prix_achat (self):
    #     for produit in self:
    #         # Pricelist item count counts the rules applicable on current template or on its variants.
    #         #produit.pricelist_item_count = produit.env['stock.vente'].search_count([('id_produit', '=', produit.id)])
    #         achat_records = produit.env['stock.achat'].search([('id_produit', '=', produit.id)])
    #         prix_achat_stock = sum(achat_records.quantite_achat for achat_records in achat_records)
    #         produit.achat_item_count = total_quantity_sold

    purchase_quantity = fields.Integer(string='Purchase Quantity', default=0)
    sale_quantity = fields.Integer(string='Sale Quantity', default=0)
    stock_quantity = fields.Integer(string='Stock Quantity', compute='_compute_stock_quantity', store=True)

    @api.depends('purchase_quantity', 'sale_quantity')
    def _compute_stock_quantity(self):
        for product in self:
            product.stock_quantity = product.purchase_quantity - product.sale_quantity

