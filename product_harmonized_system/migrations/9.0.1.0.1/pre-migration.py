# -*- coding: utf-8 -*-
# Copyright 2014 Microcom, Therp BV
# Copyright 2017 Tecnativa - Pedro M. Baeza
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


column_renames = {
    'product_template': [
        ('intrastat_code_id', None),
    ],
}


@openupgrade.migrate(use_env=True)
def migrate(env, version):
    cr = env.cr
    openupgrade.rename_columns(cr, column_renames)
