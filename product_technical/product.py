# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'product.template'

    def reset_tech_data(self):
        self.tech_data = False

    tech_data = fields.Html('Ficha Técnica')
