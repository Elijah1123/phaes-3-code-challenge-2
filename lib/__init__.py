"""
Magazine Articles System Package

This package contains all the modules for the magazine articles system:
- models: Contains Author, Article, and Magazine classes
- db: Contains database connection and setup utilities
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models.author import Author
from lib.models.article import Article
from lib.models.magazine import Magazine

from lib.db.connection import get_connection
from lib.db.seed import seed_database

__version__ = "1.0.0"


def initialize_database():
    """Initialize the database with schema and sample data"""
    from scripts.setup_db import setup_database
    setup_database()
    seed_database()
    print("Database initialized successfully!")


__all__ = [
    'Author',
    'Article',
    'Magazine',
    'get_connection',
    'seed_database',
    'initialize_database',
    '__version__'
]