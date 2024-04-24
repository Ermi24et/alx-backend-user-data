#!/usr/bin/env python3
"""hash password"""
import bcrypt
from typing import TypeVar


def _hash_password(password: str) -> TypeVar:
    """a method that takes in a password and returns bytes"""
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(bytes, salt)
    return hashed
