# -*- coding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution, third party addon
# Copyright (C) 2004-2015 Vertel AB (<http://vertel.se>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api, _
import openerp.addons.decimal_precision as dp
import logging
_logger = logging.getLogger(__name__)

class product_product(models.Model):
    _inherit = 'product.product'

    #Volume digits is hardcoded in the product view!
    volume = fields.Float('Volume', digits=dp.get_precision('Stock Volume'), help="The volume in m3.")
    weight = fields.Float('Gross Weight', digits=dp.get_precision('Stock Weight'), help="The gross weight in Kg.")
    weight_net = fields.Float('Net Weight', digits=dp.get_precision('Stock Weight'), help="The net weight in Kg.")
    categ_id = fields.Many2one(string='Category', comodel_name='product.category')

    state = fields.Selection([('',''),
            ('draft', 'In Development'),
            ('sellable','Normal'),
            ('end','End of Lifecycle'),
            ('obsolete','Obsolete')], string="Status",)
    product_manager = fields.Many2one(comodel_name="res.users",string='Product Manager')
    description_sale = fields.Text(string='Sale Description', translate=True,
            help="A description of the Product that you want to communicate to your customers. "
                 "This description will be copied to every Sale Order, Delivery Order and Customer Invoice/Refund")
