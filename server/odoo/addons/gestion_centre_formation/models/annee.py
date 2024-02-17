
# -*- coding: utf-8 -*-


from odoo import api, fields, models, _

from odoo.exceptions import ValidationError
import datetime

class FormationAnnee(models.Model):
    _name = 'formation.annee'


    @api.model
    def get_year_selection(self):
        year = 2023
        # year_1 = 2024
        year_list = []
        # while year != 2040 and year_1 != 2041:
        while year != 2040:
            year_list.append((str(year), f"{year}"))
            # year_list.append((str(year), f"{year}/{year_1}"))
            year += 1
            # year_1 += 1
        return year_list

    name_string = fields.Selection(get_year_selection, string="Année De Formation",
                            default=lambda self: str(datetime.datetime.now().year))
    _sql_constraints = [
        ('name_string', 'unique (name_string)',
         "The year ID must be unique, this one is already assigned to another year.")
    ]
    name = fields.Char(string='Année De Formation', compute='concate_name',store=True)

    @api.depends('name_string')
    def concate_name(self):
        for nam in self:
            if nam.name_string:
                nam.name = (f"{nam.name_string}")
    def return_action_to_open(self):
        """ This opens the xml view specified in xml_id for the current annnee"""
        self.ensure_one()
        xml_id = self.env.context.get('xml_id')
        if xml_id:

            res = self.env['ir.actions.act_window']._for_xml_id('gestion_centre_formation.%s' % xml_id)
            res.update(
                context=dict(self.env.context, default_year = self.id, group_by=False),
                domain=[('annee_id', '=', self.id)]
            )
            return res
        return False