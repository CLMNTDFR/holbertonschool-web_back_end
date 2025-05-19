#!/usr/bin/env python3
""" Hash_password Module
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """ Function that hashes a password with a salt.
    """
    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Function that checks if a password matches its hashed version.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
