#!/usr/bin/env python3
"""a module that manage the API authentication"""
from flask import request
from fnmatch import fnmatch
from typing import List, TypeVar
import os


class Auth:
    """a class template for all authentication system"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """a public method that returns False - path and exluded_path"""
        if not excluded_paths or not path:
            return True
        if path[-1] != '/':
            path += '/'
        return not [n for n in excluded_paths if fnmatch(path, n)]

    def authorization_header(self, request=None) -> str:
        """a method that returns None temporarily"""
        if not request and not request.headers.get('Authorization'):
            return None
        else:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """a public method that returns None temporarily"""
        return None

    def session_cookie(self, request=None) -> str:
        """a method that returns a cookie value from a request"""
        if request:
            if os.getenv('SESSION_NAME') == '_my_session_id':
                session_id = request.cookies.get('_my_session_id')
                return session_id
            return None
        return None
