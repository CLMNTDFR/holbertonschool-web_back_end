#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """
    Hashes a password with a randomly-generated salt
    and returns the salted, hashed password.
    """
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def _generate_uuid() -> str:
    """ Generates a new UUID and returns its string representation.
    """
    return str(uuid.uuid4())


class Auth:
    """ Auth class to interact with the authentication database.
    """

    def __init__(self):
        """ Initializes a new instance of the class.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers a user with a given email and password.

            Args:
                email (str): The email address of the new user.
                password (str): The plaintext password of the new user.

            Returns:
                User: The instance of the newly created User object.
        """
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError("User {} already exists".format(email))

        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """ Validates if a given email and password correspond to a valid user.
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ Creates a session for a user.
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """ Retrieves a User object based on a session ID.
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """ Destroys a user's session by setting their session ID to None.
        """
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """ Generates a reset password token for a user with the given email.
        """
        token = _generate_uuid()

        try:
            user = self._db.find_user_by(email=email)
            self._db.update_user(user.id, reset_token=token)
            return token

        except NoResultFound:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """ Updates a user's password based on a reset token.
        """
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed_password = _hash_password(password)
            self._db.update_user(user.id, hashed_password=hashed_password,
                                 reset_token=None)

        except NoResultFound:
            raise ValueError("Invalid reset token")
