# -*- coding: utf-8 -*-


from odoo import api, fields, models, _

from odoo.exceptions import ValidationError
import datetime

class FormationFormation(models.Model):
    _name = 'formation.formation'

    name = fields.Char(string='Formation', required=True)
    description = fields.Text(string='Description de la formation')
    duree = fields.Float(string='Durée (en heures)')

    @api.depends ('annee')
    def concate_name (self):
        for n in self:
            if n.annee:
              n.name = (f"Formation {n.annee.name}")

    annee_id = fields.Many2one('formation.annee',  string='Année')
    modeformation_id = fields.Many2one('formation.mode',  string='Mode Formation')
    typeformation_id = fields.Many2one('formation.type',  string='Type Formation')
    entreprise_ids = fields.Many2many('formation.entreprise',  string='Entreprise')
    site_id = fields.Many2one('formation.site',  string='Lieu de Formation')
    date_debut = fields.Date(string='Date Début')
    date_fin = fields.Date(string='Date Fin')

    nbr_ressources = fields.Integer(string='Nombre Ressource')
    nbr_apprenants = fields.Integer(string='Nombre d\'apprenants inscrits', compute='_compute_nombre_apprenants')
    nbr_groupe = fields.Integer(string='Nombre de groupes', compute='_compute_nombre_groupes')

    inscriptions_ids = fields.One2many('formation.inscription','formation_id',string='liste des inscrits')
    groupes_ids = fields.One2many('formation.groupe','formation_id',string='Groupes')

    # color = fields.Integer(string="Color", help="The color of the card in kanban view", compute='_compute_color', store=True)
    color = fields.Integer(string="Color", help="The color of the card in kanban view", default = 3)#, compute='_compute_color', store=True)
    #
    # @api.depends('state', 'module_state')
    # def _compute_color(self):
    #     """ Update the color of the kanban card based on the state of the acquirer.
    #
    #     :return: None
    #     """
    #     for acquirer in self:
    #         if acquirer.module_id and not acquirer.module_state == 'installed':
    #             acquirer.color = 4  # blue
    #         elif acquirer.state == 'disabled':
    #             acquirer.color = 3  # yellow
    #         elif acquirer.state == 'test':
    #             acquirer.color = 2  # orange
    #         elif acquirer.state == 'enabled':
    #             acquirer.color = 7  # green



    # Fonction pour calculer le nombre d'apprenants inscrits
    @api.depends('inscriptions_ids')
    def _compute_nombre_apprenants(self):
        for formation in self:
            formation.nbr_apprenants = len(formation.inscriptions_ids)

    # Fonction pour calculer le nombre de groupes
    @api.depends('groupes_ids')
    def _compute_nombre_groupes(self):
        for formation in self:
            formation.nbr_groupe = len(formation.groupes_ids)

    @api.constrains('date_debut', 'date_fin')
    def _check_dates(self):
        for record in self:
            if record.date_debut and record.date_fin:
                if record.date_debut > record.date_fin:
                    raise ValidationError("La date de début ne peut pas être après la date de fin.")


    def return_action_to_open(self):
        """ This opens the xml view specified in xml_id for the current depert """
        self.ensure_one()
        xml_id = self.env.context.get('xml_id')
        if xml_id:

            res = self.env['ir.actions.act_window']._for_xml_id('gestion_centre_formation.%s' % xml_id)
            res.update(
                context=dict(self.env.context, default_formation_id=self.id, group_by=False),
                domain=[('formation_id', '=', self.id)]
            )
            return res
        return False