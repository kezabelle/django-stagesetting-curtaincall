# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

__all__ = ['get_maintenance_mode', 'set_maintenance_mode']


# named for api compatibility with django-maintenance-mode
def get_maintenance_mode():
    return True


# named for api compatibility with django-maintenance-mode
def set_maintenance_mode(value):
    return False
