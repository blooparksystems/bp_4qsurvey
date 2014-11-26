 # -*- coding: utf-8 -*-
from openerp.models import Model
from openerp import fields

class Website(Model):
    _inherit = 'website'

    iperceptions4qsurvey = fields.Boolean(
        string='Use 4Q Survey',
        default=False,
        help=('if activated 4Q Survey is active'),
        translate=True
    )
    iperceptions4qsurvey_script = fields.Text(
        string='4Q Survey Script'
    )
