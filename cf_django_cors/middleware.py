# -*- coding: utf-8 -*-
import os

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

ALLOW_ORIGIN = os.getenv('ALLOW_ORIGIN', '*')
ALLOW_HEADERS = os.getenv('ALLOW_HEADERS', ('x-requested-with, Content-Type, '
                                            'origin, authorization, accept, '
                                            'client-security-token'))
ALLOW_METHODS = os.getenv('ALLOW_METHODS', 'DELETE, GET, OPTIONS, POST, PUT')
MAX_AGE = os.getenv('MAX_AGE', 1000)


class CorsMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        """Add the respective CORS headers"""
        response['Access-Control-Allow-Origin'] = ALLOW_ORIGIN
        response['Access-Control-Allow-Headers'] = ALLOW_HEADERS
        response['Access-Control-Allow-Methods'] = ALLOW_METHODS
        response['Access-Control-Max-Age'] = MAX_AGE

        return response
