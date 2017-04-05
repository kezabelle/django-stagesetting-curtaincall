# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import logging
from django.conf import urls
from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


logger = logging.getLogger(__name__)


class CurtainCallAppConfig(AppConfig):
    name = 'stagesetting_curtaincall'
    verbose_name = _("Maintainance mode")


    def ready(self):
        from .checks import check_setting
        self.patch_urlconf()

    def patch_urlconf(self):
        urls.handler503 = 'stagesetting_curtaincall.views.handler503'
        urls.__all__.append('handler503')
