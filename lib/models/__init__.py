"""
Models Package

This package contains all the data models for the Magazine Articles system.
"""

# Import all model classes to make them available from the models package
from .author import Author
from .article import Article
from .magazine import Magazine

# Package-level initialization
def create_all_tables():
    """Create all database tables for the models"""
    Author.create_table()
    Magazine.create_table()
    Article.create_table()
    print("All database tables created successfully!")

# Make these available when importing from lib.models
__all__ = [
    'Author',
    'Article',
    'Magazine',
    'create_all_tables'
]

# Version of the models package
__version__ = "1.0.0"