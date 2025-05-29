"""
Database Package

This package contains all database-related components:
- Connection management
- Schema definitions
- Seed data utilities
"""


from .connection import get_connection
from .seed import seed_database


from .schema import create_schema, drop_schema


def initialize_database():
    """Initialize the database with schema and sample data"""
    drop_schema()
    create_schema()
    seed_database()
    print("Database initialized successfully!")


__all__ = [
    'get_connection',
    'seed_database',
    'initialize_database',
    'create_schema',
    'drop_schema'
]


__version__ = "1.0.0"