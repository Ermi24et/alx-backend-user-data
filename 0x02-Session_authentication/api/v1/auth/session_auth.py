#!/usr/bin/env python3
"""A module that contains SessionAuth class that inherits from Auth"""
from uuid import uuid4
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """A class used to create a session authentication mechanism"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """a method that creates a Session ID for a user_id"""
        if user_id and isinstance(user_id, str):
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """a method that returns a User ID based on s Session ID"""
        if session_id and isinstance(session_id, str):
            user_id = self.user_id_by_session_id.get(session_id)
            return user_id
        return None
