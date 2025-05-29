"""
Database Schema Utilities

Contains functions for creating and dropping the database schema.
"""

from .connection import get_connection

def create_schema():
    """Create the database schema by executing schema.sql"""
    conn = get_connection()
    cursor = conn.cursor()
    
    
    with open('lib/db/schema.sql', 'r') as f:
        schema = f.read()
    cursor.executescript(schema)
    
    conn.commit()
    conn.close()

def drop_schema():
    """Drop all database tables"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.executescript("""
        DROP TABLE IF EXISTS articles;
        DROP TABLE IF EXISTS authors;
        DROP TABLE IF EXISTS magazines;
    """)
    
    conn.commit()
    conn.close()