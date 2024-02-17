# -*- coding: utf-8 -*-


from odoo import api, fields, models, tools, _,SUPERUSER_ID


class FormationSite(models.Model):
    _name = 'formation.site'

    name = fields.Char(string='Nom du site', required=True)
    responsable = fields.Char(string='Nom du Responsable', required=True)
    adresse = fields.Text(string='Adresse du site')

class FormationRessource(models.Model):
    _name = 'formation.ressource'

    name = fields.Char(string='Nom de la ressource', required=True)
    description = fields.Text(string='Description de la ressource')
    cout = fields.Float(string='Coût de la ressource')



class FormationContrat(models.Model):
    _name = 'formation.contrat'

    name = fields.Char(string='Nom du contrat', required=True)
    date_debut = fields.Date(string='Date de début')
    date_fin = fields.Date(string='Date de fin')
    entreprise_id = fields.Many2one('formation.entreprise', string='Entreprise')
    site_id = fields.Many2one('formation.site', string='Site')
    # Exigences contractuelles
    exigences_contractuelles = fields.Text(string='Exigences contractuelles')

    # Détails de facturation
    adresse_facturation = fields.Text(string='Adresse de facturation')
    mode_paiement = fields.Selection([
        ('virement', 'Virement bancaire'),
        ('cheque', 'Chèque'),
        ('espece', 'Espèces'),
    ], string='Mode de paiement')

    # Délai de paiement
    delai_paiement = fields.Integer(string='Délai de paiement (en jours)')

    # Détails sur le nombre d'apprenants et les formations
    nombre_apprenants = fields.Integer(string='Nombre d\'apprenants prévus')
    formations_ids = fields.Many2many('formation.formation', string='Formations prévues')

    # Ressources utilisées
    ressources_ids = fields.Many2many('formation.ressource', string='Ressources utilisées')
    cout_total_ressources = fields.Float(string='Coût total des ressources', compute='_compute_cout_total_ressources',
                                         store=True)

    @api.depends('ressources_ids')
    def _compute_cout_total_ressources(self):
        for contrat in self:
            cout_total = sum(ressource.cout for ressource in contrat.ressources_ids)
            contrat.cout_total_ressources = cout_total

    # Autres détails du contrat
    conditions_generales = fields.Text(string='Conditions générales')
