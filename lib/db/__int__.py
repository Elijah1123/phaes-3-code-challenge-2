# lib/db/__init__.py

"""
This file marks the db directory as a package.
You can use this file to initialize shared database logic.
"""

from .connection import get_connection

__all__ = ["get_connection"]
