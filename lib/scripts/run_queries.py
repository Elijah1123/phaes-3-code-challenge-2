import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

"""
Query Runner Script

This script demonstrates example queries using the Magazine Articles system models.
It can be used to test the functionality or as a reference for query patterns.
"""

from models import Author, Article, Magazine
from db.connection import get_connection

def run_example_queries():
    """Execute and display results of example queries"""
    print("\n" + "="*50)
    print("Magazine Articles System - Example Queries")
    print("="*50 + "\n")
    
    conn = get_connection()
    
    try:
       
        print("1. All articles by John Doe:")
        author = Author.find_by_name("John Doe")
        if author:
            for article in author.articles():
                print(f"- {article.title}")
        else:
            print("Author not found")
        print("\n" + "-"*50 + "\n")
        
       
        print("2. All magazines Jane Smith has written for:")
        author = Author.find_by_name("Jane Smith")
        if author:
            for magazine in author.magazines():
                print(f"- {magazine.name} ({magazine.category})")
        else:
            print("Author not found")
        print("\n" + "-"*50 + "\n")
        
       
        print("3. All authors who have written for Tech Today:")
        magazine = Magazine.find_by_name("Tech Today")
        if magazine:
            for author in magazine.contributors():
                print(f"- {author.name}")
        else:
            print("Magazine not found")
        print("\n" + "-"*50 + "\n")
        
     
        print("4. Magazines with articles by at least 2 authors:")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT m.name, COUNT(DISTINCT a.author_id) as author_count
            FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            GROUP BY m.id
            HAVING author_count >= 2
        """)
        for row in cursor.fetchall():
            print(f"- {row['name']} ({row['author_count']} authors)")
        print("\n" + "-"*50 + "\n")
        
     
        print("5. Article count per magazine:")
        cursor.execute("""
            SELECT m.name, COUNT(a.id) as article_count
            FROM magazines m
            LEFT JOIN articles a ON m.id = a.magazine_id
            GROUP BY m.id
            ORDER BY article_count DESC
        """)
        for row in cursor.fetchall():
            print(f"- {row['name']}: {row['article_count']} articles")
        print("\n" + "-"*50 + "\n")
        
       
        print("6. Author with most articles:")
        cursor.execute("""
            SELECT a.name, COUNT(ar.id) as article_count
            FROM authors a
            JOIN articles ar ON a.id = ar.author_id
            GROUP BY a.id
            ORDER BY article_count DESC
            LIMIT 1
        """)
        result = cursor.fetchone()
        if result:
            print(f"{result['name']} with {result['article_count']} articles")
        else:
            print("No authors found")
        print("\n" + "-"*50 + "\n")
        
     
        print("7. Tech Today's contributing authors (>2 articles):")
        magazine = Magazine.find_by_name("Tech Today")
        if magazine:
            for author in magazine.contributing_authors():
                print(f"- {author.name}")
            if not magazine.contributing_authors():
                print("No contributing authors found")
        else:
            print("Magazine not found")
        print("\n" + "-"*50 + "\n")
        
      
        print("8. Magazine with most articles (top publisher):")
        top_magazine = Magazine.top_publisher()
        if top_magazine:
            print(f"{top_magazine.name} ({top_magazine.category})")
        else:
            print("No magazines found")
        print("\n" + "="*50 + "\n")
        
    finally:
        conn.close()

if __name__ == "__main__":
    run_example_queries()