#!/usr/bin/env python3
"""a module that contains subclass of Auth"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """a subclass of Auth"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """a method that returns the Base64 part of the authorization header
        for basic auth"""
        if authorization_header and isinstance(authorization_header, str):
            if authorization_header[0: 6] == 'Basic ':
                return authorization_header[len("Basic "):]
            return None
        return None
