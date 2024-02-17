# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
import base64


class FormationEntreprise(models.Model):
    _name = 'formation.entreprise'


    name = fields.Char(string="Nom de l'entreprise", required=True)
    adresse = fields.Text(string="Adresse de l'entreprise")
    # contact = fields.Char(string="Contact de l'entreprise")
    tele = fields.Char(string='Numéro de téléphone')
    fax = fields.Char(string='Numéro de fax')
    email = fields.Char(string='Email')

    image_field = fields.Binary('Image Field')
    formation_ids = fields.Many2many('formation.formation',  string='formation')
    # formation_id = fields.Many2one('formation.formation',  string='formation')

    # def return_action_to_open(self):
    #     """ This opens the xml view specified in xml_id for the current depert """
    #     self.ensure_one()
    #     xml_id = self.env.context.get('xml_id')
    #     if xml_id:
    #
    #         res = self.env['ir.actions.act_window']._for_xml_id('gestion_centre_formation.%s' % xml_id)
    #         res.update(
    #             context=dict(self.env.context, default_depart_id=self.id, group_by=False),
    #             domain=[('entreprise_id', '=', self.id)]
    #         )
    #         return res
    #     return False

