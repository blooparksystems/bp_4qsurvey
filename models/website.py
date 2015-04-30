# -*- coding: utf-8 -*-
##############################################################################
#
# Odoo, an open source suite of business apps
# This module copyright (C) 2015 bloopark systems (<http://bloopark.de>).
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
from openerp.models import Model
from openerp import fields


class Website(Model):

    """Adds the fields for 4Q Survey."""

    _inherit = 'website'

    iperceptions4qsurvey = fields.Boolean(
        string='Use 4Q Survey',
        default=False,
        help=('if activated 4Q Survey is active')
    )
    iperceptions4qsurvey_script = fields.Text(
        string='4Q Survey Script'
    )
