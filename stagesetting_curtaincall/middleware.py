# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
try:
    from django.urls import reverse, NoReverseMatch, get_resolver
except ImportError:
    from django.core.urlresolvers import reverse, NoReverseMatch, get_resolver
try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:  # < Django 1.10
    class MiddlewareMixin(object):
        pass
from .core import get_maintenance_mode

__all__ = ['MaintenanceModeMiddleware', 'DowntimeMiddleware']


# named for API compatibility with django-maintainancemode and django-maintainance-mode
class MaintenanceModeMiddleware(MiddlewareMixin):

    def get_url_for_disabling(self):
        try:
            url_off = reverse('maintenance_mode_off')
            return url_off
        except NoReverseMatch:
            return None

    def allow_user_to_turn_off_via_url(self, request):
        if request.user.is_authenticated() and request.user.is_superuser:
            return True
        return False

    def get_urlconf_resolver(self, request):
        if hasattr(request, 'urlconf'):
            urlconf = request.urlconf
            return get_resolver(urlconf)
        return get_resolver(None)

    def process_request(self, request):
        if get_maintenance_mode() is False:
            return None

        url_for_disabling = self.get_url_for_disabling
        url_off = url_for_disabling()
        if url_off == request.path:
            allowed_user_func = self.allow_user_to_turn_off_via_url
            if allowed_user_func(request=request):
                return None

            url_resolver = self.get_urlconf_resolver
            resolver_for_request = url_resolver(request=request)
            return resolver_for_request.resolve_error_handler('503')


DowntimeMiddleware = MaintenanceModeMiddleware  # API compatibility with django-downtime
