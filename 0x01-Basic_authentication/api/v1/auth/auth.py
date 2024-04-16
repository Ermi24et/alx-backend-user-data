#!/usr/bin/env python3
"""a module that manage the API authentication"""
from flask import request
from typing import List, TypeVar


class Auth:
    """a class template for all authentication system"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """a public method that returns False - path and exluded_path"""
        return False

    def authorization_header(self, request=None) -> str:
        """a method that returns None temporarily"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """a public method that returns None temporarily"""
        return None
