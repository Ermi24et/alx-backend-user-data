#!/usr/bin/env python3
"""a module that contains subclass of Auth"""
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """a method that returns the decoded value of a Base64 string"""
        if base64_authorization_header:
            if isinstance(base64_authorization_header, str):
                try:
                    bytes_seq = base64.b64decode(base64_authorization_header)
                    return bytes_seq.decode('utf-8')
                except Exception:
                    return None
        return None
