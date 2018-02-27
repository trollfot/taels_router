# -*- coding: utf-8 -*-

class RoutingException(Exception):
    pass


class RouteExists(RoutingException):
    pass


class RouteDoesNotExist(RoutingException):
    pass


class NotFound(RoutingException):
    pass


class MethodNotSupported(RoutingException):
    pass
