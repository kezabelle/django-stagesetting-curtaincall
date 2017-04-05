# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from functools import partial
from django.core.checks import Error
from django.core.checks import Info

E001 = partial(Error,
    msg="Missing MAINTENANCE_MODE in your STAGESETTINGS",
    # hint="Setting names should be UPPER_CASE_WITH_UNDERSCORES",
    id="stagesetting_curtaincall.E001",
)
