
"""
Interactive Debugging Console for Magazine Articles System

This script provides an interactive shell with preloaded models
and database connection for debugging and exploration.
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import code
from lib import (
    Author, Article, Magazine,
    get_connection, seed_database
)

def start_debug_session():
    """Start an interactive debugging session"""
    
  
    print("\n" + "="*50)
    print("Magazine Articles Debug Console")
    print("="*50)
    print("\nAvailable objects:")
    print("- Author: Author model class")
    print("- Article: Article model class")
    print("- Magazine: Magazine model class")
    print("- conn: Active database connection")
    print("- seed_database(): Function to reseed the database")
    print("\nExample usage:")
    print(">>> authors = Author.find_by_name('John Doe')")
    print(">>> magazines = Magazine.find_by_category('Technology')")
    print(">>> conn.execute('SELECT * FROM articles LIMIT 5').fetchall()")
    print("\nType 'exit()' or press Ctrl-D to quit")
    print("="*50 + "\n")
    
 
    conn = get_connection()
    
  
    local_vars = {
        'Author': Author,
        'Article': Article,
        'Magazine': Magazine,
        'conn': conn,
        'seed_database': seed_database,
    }
    
 
    try:
        code.interact(
            banner="",
            local=local_vars,
            exitmsg="\nExiting debug console. Goodbye!\n"
        )
    finally:
       
        conn.close()

if __name__ == "__main__":
    start_debug_session()