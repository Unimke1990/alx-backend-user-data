#!/usr/bin/env python3
"""Auth modules"""

from flask import request
from typing import List, Typevar


class Auth:
    """manages API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns path and excluded_paths"""
        return False

    def authorization_header(self, request=None) -> str:
        """returns none"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns none"""
        return None
