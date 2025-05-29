import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import get_connection

@pytest.fixture(autouse=True)
def setup_database():
    """Setup test database with sample data before each test"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript("""
        DELETE FROM articles;
        DELETE FROM authors;
        DELETE FROM magazines;
        
        INSERT INTO authors (id, name) VALUES 
        (1, 'John Doe'),
        (2, 'Jane Smith'),
        (3, 'Bob Johnson');
        
        INSERT INTO magazines (id, name, category) VALUES 
        (1, 'Tech Today', 'Technology'),
        (2, 'Science Weekly', 'Science'),
        (3, 'Business Insights', 'Business');
        
        INSERT INTO articles (id, title, author_id, magazine_id) VALUES 
        (1, 'The Future of AI', 1, 1),
        (2, 'Quantum Computing', 2, 1),
        (3, 'Genetic Engineering', 2, 2),
        (4, 'Market Trends 2023', 3, 3),
        (5, 'Startup Funding', 3, 3);
    """)
    conn.commit()
    conn.close()

def test_article_creation():
    """Test creating and savi # Verify articles were also deleted (due to ON DELETE CASCADE)ng an article"""
    author = Author.find_by_id(1)
    magazine = Magazine.find_by_id(1)
    article = Article("New Article", author.id, magazine.id)
    article.save()
    
    assert article.id is not None
    assert article.title == "New Article"
    assert article.author_id == author.id
    assert article.magazine_id == magazine.id

def test_article_find_by_id():
    """Test finding an article by ID"""
    article = Article.find_by_id(1)
    assert article is not None
    assert article.title == "The Future of AI"
    assert article.author_id == 1
    assert article.magazine_id == 1

def test_article_find_by_title():
    """Test finding an article by title"""
    article = Article.find_by_title("Quantum Computing")
    assert article is not None
    assert article.id == 2
    assert article.author_id == 2
    assert article.magazine_id == 1

def test_article_author():
    """Test getting the author of an article"""
    article = Article.find_by_id(1)
    author = article.author()
    assert author is not None
    assert author.name == "John Doe"

def test_article_magazine():
    """Test getting the magazine of an article"""
    article = Article.find_by_id(3)
    magazine = article.magazine()
    assert magazine is not None
    assert magazine.name == "Science Weekly"
    assert magazine.category == "Science"

def test_article_update():
    """Test updating an article"""
    article = Article.find_by_id(1)
    article.title = "Updated Title"
    article.save()
    
    updated = Article.find_by_id(1)
    assert updated.title == "Updated Title"

def test_article_delete():
    """Test deleting an article"""
    article = Article.find_by_id(1)
    article.delete()
    
    deleted = Article.find_by_id(1)
    assert deleted is None

def test_article_author_relationship():
    """Test the relationship between article and author"""
    article = Article.find_by_id(2)
    author = Author.find_by_id(2)
    
    assert article.author().id == author.id
    assert article in author.articles()

def test_article_magazine_relationship():
    """Test the relationship between article and magazine"""
    article = Article.find_by_id(4)
    magazine = Magazine.find_by_id(3)
    
    assert article.magazine().id == magazine.id
    assert article in magazine.articles()