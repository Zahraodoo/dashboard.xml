# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class StatistiqueState(models.Model):
    _name = "formation.state"
    _order = 'sequence'

    name = fields.Char("State Name", required=True, translate=True)
    sequence = fields.Integer("Sequence", default=1, help="Gives the sequence order when displaying a list of statistiques.")

    requirements = fields.Text("Requirements")
    template_id = fields.Many2one('mail.template', "Email Template",
        help="If set, a message is posted on the applicant using the template when the applicant is set to the statistique.")
    fold = fields.Boolean("Folded in Kanban",
        help="This statistique is folded in the kanban view when there are no records in that statistique to display.")

    @api.model
    def default_get(self, fields):
        if self._context and self._context.get('default_depart_id') and not self._context.get('formation_state_mono', False):
            context = dict(self._context)
            context.pop('default_depart_id')
            self = self.with_context(context)
        return super(StatistiqueState, self).default_get(fields)


#---------------------------------------------------------------------
