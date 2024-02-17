# -*- coding: utf-8 -*-


from odoo import api, fields, models, _, exceptions

from odoo.exceptions import ValidationError
import datetime
from datetime import datetime

class FormationGroupe(models.Model):
    _name = 'formation.groupe'

    name = fields.Integer(string="Numéro groupe", default=0, compute='incrementer_numero_groupe', store=True)
    nbr_groupe = fields.Integer(string="Nombre Groupe", default=0, compute='incrementer_numero_groupe', store=True)

    @api.depends('formation_id','annee_id','name','nbr_groupe')
    def incrementer_numero_groupe(self):
        for record in self:
            if record.annee:
                dernier_formation = self.env['formation.formation'].search(
                    ['&',('annee_id.id', '=', record.annee_id.id),('groupe_id.id', '=', record.id)])
                print('dernier_enquete')
                dernier_numero = len(dernier_formation)- 1
                record.nbr_groupe = len(dernier_formation)- 1
                record.name = dernier_numero + 1
            else:
                pass

    formation_id = fields.Many2one('formation.formation', string='Formation')

    date_groupe = fields.Date(string='Date création de groupe', default=lambda s: fields.Date.context_today(s))

    annee_id = fields.Many2one('formation.annee', string='Année',compute='_compute_year', store=True)

    @api.depends('date_groupe')
    def _compute_year(self):
        for record in self:
            if record.date_enquete:
                year = record.date_formation.year
                annee_formation = self.env['formation.annee'].search([('name', '=', record.annee_id.id)], limit=1)
                print(annee_formation.id)
                if annee_formation:
                    record.annee_ids = annee_formation.id
                    print(record.annee_id)
                    formation = self.env['formation.formation'].search([('annee.id', '=', year)], limit=1)
                    print(formation)
                    if formation:
                        record.formation = formation.id
                    else:
                        pass
            else:
                pass
    formation_id = fields.Many2one('formation.formation', string='Formation',compute='_compute_year', store=True)

