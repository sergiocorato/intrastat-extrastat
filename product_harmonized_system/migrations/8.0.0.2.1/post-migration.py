# -*- coding: utf-8 -*-
# Copyright 2021 Sergio Corato <https://github.com/sergiocorato>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade
from openerp import SUPERUSER_ID
from openerp.api import Environment

import logging
_logger = logging.getLogger(__name__)


@openupgrade.migrate()
def migrate(cr, version):
    env = Environment(cr, SUPERUSER_ID, {})
    # creare un duplicato di hs_code_id (company_dependent) normale
    # copiando in ordine di priorità per azienda il campo se compilato
    product_templates = env['product.template'].search([
        ('hs_code_id', '!=', False),
    ])
    for company in sorted(env.user.company_ids, key=lambda a: a['id'], reverse=True):
        env.user.company_id = company
        for template in product_templates:
            if template.hs_code_id:
                template.intrastat_code_id = template.hs_code_id
                _logger.info('Updated intrastat code to %s for product template %s' % (
                    template.hs_code_id.local_code,
                    template.default_code,
                ))
