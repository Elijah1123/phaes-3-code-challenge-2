

"""
This file marks the lib directory as a package.
It can be used to initialize or aggregate common utilities across the application.
"""

from .models import Author, Article, Magazine
from .db import get_connection

__all__ = ["Author", "Article", "Magazine", "get_connection"]
