# -*- coding: utf-8 -*-

HTTP_METHODS = ('GET', 'POST', 'PUT', 'HEAD', 'OPTIONS', 'PATCH', 'DELETE')


class CompositionView:
    """Simple method-function mapped view for the sanic.
    You can add handler functions to methods (get, post, put, patch, delete)
    for every HTTP method you want to support.
    For example:
        view = CompositionView()
        view.add(['GET'], lambda request: text('I am get method'))
        view.add(['POST', 'PUT'], lambda request: text('I am post/put method'))
    etc.
    If someone tries to use a non-implemented method, there will be a
    405 response.
    """

    def __init__(self):
        self.handlers = {}

    def add(self, methods, handler, stream=False):
        if stream:
            handler.is_stream = stream
        for method in methods:
            if method not in HTTP_METHODS:
                raise RuntimeError(
                    '{} is not a valid HTTP method.'.format(method))

            if method in self.handlers:
                raise RuntimeError(
                    'Method {} is already registered.'.format(method))
            self.handlers[method] = handler

    def __call__(self, request, *args, **kwargs):
        handler = self.handlers[request.method.upper()]
        return handler(request, *args, **kwargs)
