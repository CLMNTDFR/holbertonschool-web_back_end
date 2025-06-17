#!/usr/bin/env python3
"""
Authentication module for the API
"""
from flask import request
from typing import List, TypeVar


User = TypeVar('User')


class Auth():
    """ Class to manage the API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines if authentication is required for the given path.
        """
        if path is None:
            return True

        if not excluded_paths:
            return True

        normal_path = path if path.endswith('/') else path + '/'

        normal_excluded_paths = [p if p.endswith('/') else p + '/'
                                 for p in excluded_paths]

        if normal_path in normal_excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Retrieves the Authorization header from the request.
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> User:
        """ Retrieves the current user from the request.
        """
        return None
