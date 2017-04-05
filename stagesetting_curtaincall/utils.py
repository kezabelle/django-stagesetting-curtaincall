# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

# api compatibility with django-maintenancemode

from .core import get_maintenance_mode, set_maintenance_mode


__all__ = ['status', 'activate', 'deactivate']


status = get_maintenance_mode

def activate():
    return set_maintenance_mode(True)

def deactivate():
    return set_maintenance_mode(False)
