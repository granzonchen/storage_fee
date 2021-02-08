# -*- coding: utf-8 -*-
from odoo import _, api, fields, models, SUPERUSER_ID
from odoo.exceptions import UserError
from odoo.osv import expression
from odoo.tools import pycompat,float_is_zero
from odoo.tools.float_utils import float_round


class Product(models.Model):
    _inherit = "product.product"
