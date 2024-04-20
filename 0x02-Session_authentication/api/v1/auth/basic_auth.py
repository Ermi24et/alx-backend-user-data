#!/usr/bin/env python3
"""a module that contains subclass of Auth"""
from api.v1.auth.auth import Auth
import base64
from typing import Tuple, TypeVar
from models.user import User
from models.base import Base


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
                    bytes_seq = base64.b64decode(base64_authorization_header,
                                                 validate=True)
                    return bytes_seq.decode('utf-8')
                except (base64.binascii.Error, UnicodeDecodeError):
                    return None
        return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> Tuple[str]:
        """a method that rerurns the user email and password from the Base64
        decoded value"""
        if decoded_base64_authorization_header:
            if isinstance(decoded_base64_authorization_header, str):
                if ":" in decoded_base64_authorization_header:
                    list_str = decoded_base64_authorization_header.split(':')
                    return (list_str[0], ':'.join(list_str[1:]))
                return (None, None)
        return (None, None)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """a method that returns the User instance based on his email
        and password"""
        if user_email and user_pwd:
            if isinstance(user_email, str) and isinstance(user_pwd, str):
                try:
                    u = User()
                    users = u.search(attributes={"email": user_email})
                except KeyError:
                    return None
                if len(users) != 0:
                    if users[0].is_valid_password(user_pwd):
                        return users[0]
                    return None
                return None
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """a method that overloads Auth and retrieves the User
        instance for a request"""
        auth = self.authorization_header(request)
        extracted = self.extract_base64_authorization_header(auth)
        decoded = self.decode_base64_authorization_header(extracted)
        user_email, user_pwd = self.extract_user_credentials(decoded)
        return self.user_object_from_credentials(user_email, user_pwd)
