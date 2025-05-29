from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed_database():
    # Clear existing data
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    conn.commit()
    conn.close()

    # Create authors
    author1 = Author("John Doe")
    author1.save()
    
    author2 = Author("Jane Smith")
    author2.save()
    
    author3 = Author("Bob Johnson")
    author3.save()

    # Create magazines
    magazine1 = Magazine("Tech Today", "Technology")
    magazine1.save()
    
    magazine2 = Magazine("Science Weekly", "Science")
    magazine2.save()
    
    magazine3 = Magazine("Business Insights", "Business")
    magazine3.save()

    # Create articles
    article1 = Article("The Future of AI", author1.id, magazine1.id)
    article1.save()
    
    article2 = Article("Quantum Computing", author2.id, magazine1.id)
    article2.save()
    
    article3 = Article("Neural Networks", author1.id, magazine1.id)
    article3.save()
    
    article4 = Article("Genetic Engineering", author2.id, magazine2.id)
    article4.save()
    
    article5 = Article("Market Trends 2023", author3.id, magazine3.id)
    article5.save()
    
    article6 = Article("Startup Funding", author3.id, magazine3.id)
    article6.save()
    
    article7 = Article("Blockchain Revolution", author3.id, magazine1.id)
    article7.save()

    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()