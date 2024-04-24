#!/usr/bin/env python3
"""hash password"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """a method that takes in a password and returns bytes"""
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(bytes, salt)
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self) -> None:
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """saves a user with email and hashed password to database"""
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            user = self._db.add_user(email, _hash_password(password))
        else:
            raise ValueError(f"User {email} already exists")
        return user
