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
    product_templates = env['product.template'].search([
        ('intrastat_code_id', '!=', False),
    ])
    for template in product_templates:
        template.intrastat_hs_code = template.intrastat_code_id.local_code
        _logger.info('Updated intrastat code to %s for product template %s' % (
            template.intrastat_hs_code.local_code,
            template.default_code,
        ))
