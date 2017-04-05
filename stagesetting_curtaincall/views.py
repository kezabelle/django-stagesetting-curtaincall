# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import
from django.http import HttpResponseServerError
from django.template import Context, Engine, TemplateDoesNotExist, loader


class HttpResponseServiceUnavailable(HttpResponseServerError):
    status_code = 503


ERROR_503_TEMPLATE_NAME = '503.html'


def handler503(request, template_name='503.html'):
    try:
        template = loader.get_template(template_name)
    except TemplateDoesNotExist:
        if template_name != ERROR_503_TEMPLATE_NAME:
            # Reraise if it's a missing custom template.
            raise
        return HttpResponseServiceUnavailable('<h1>Service Unavailable (503)</h1>', content_type='text/html')
    context = {
        'request_path': request.path,
        'request_pathinfo': request.path_info,
    }
    body = template.render(Context(context))
    return HttpResponseServiceUnavailable(body)
