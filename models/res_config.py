 # -*- coding: utf-8 -*-
from openerp.models import TransientModel
from openerp import fields

class WebsiteConfigSettings(TransientModel):
    _inherit = 'website.config.settings'

    iperceptions4qsurvey = fields.Boolean(
        string='Use 4Q Survey',
        related='website_id.iperceptions4qsurvey',
        help=('if activated 4Q Survey is active')
    )
    iperceptions4qsurvey_script = fields.Text(
        string='4Q Survey Script',
        related='website_id.iperceptions4qsurvey_script'
    )