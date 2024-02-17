
# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import date


class FormationApprenants(models.Model):
    _name = 'formation.apprenants'

    name = fields.Char(string='Nom & Prénom', compute='_compute_full_name', store=True)

    @api.depends('nom', 'prenom')
    def _compute_full_name(self):
        for partner in self:
            partner.name = f"{partner.nom} {partner.prenom}"

    nom = fields.Char(string='Nom', required=True)
    prenom = fields.Char(string='Prénom', required=True)
    date_naissance = fields.Date(string='Date de naissance')
    age = fields.Integer(string='Âge', compute='_compute_age', store=True)
    adresse = fields.Text(string='Adresse')
    telephone = fields.Char(string='Numéro de téléphone')
    email = fields.Char(string='Email')
    niveau_etude = fields.Selection([
        ('primaire', 'Primaire'),
        ('secondaire', 'Secondaire'),
        ('universitaire', 'Universitaire'),
        ('autre', 'Autre')
    ], string='Niveau d\'études')

    @api.depends('date_naissance')
    def _compute_age(self):
        today = date.today()
        for apprenant in self:
            if apprenant.date_naissance:
                birth_date = fields.Datetime.from_string(apprenant.date_naissance)
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
                apprenant.age = age
            else:
                apprenant.age = 0
    #inscriptions = fields.One2many('formation.inscription', 'apprenant_id', string='Inscriptions')
