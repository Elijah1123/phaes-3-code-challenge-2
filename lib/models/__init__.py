# lib/models/__init__.py

"""
This file marks the models directory as a package.
It can also be used to import models for convenient access.
"""

from .author import Author
from .article import Article
from .magazine import Magazine

__all__ = ["Author", "Article", "Magazine"]
