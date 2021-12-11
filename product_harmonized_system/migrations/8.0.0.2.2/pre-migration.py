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
    # crea i record di report.intrastat.code su bale degli hs.code esistenti
    if openupgrade.table_exists(cr, 'report_intrastat_code'):
        openupgrade.logged_query(
            cr,
            """
                INSERT INTO report_intrastat_code(id, name, description)
                (SELECT id, local_code, description FROM hs_code)
            """
        )
        _logger.info('Created intrastat codes from hs codes')
