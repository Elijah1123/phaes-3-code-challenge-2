import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import get_connection

@pytest.fixture(autouse=True)
def setup_database():
    # Setup database before each test
    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript("""
        DELETE FROM articles;
        DELETE FROM authors;
        DELETE FROM magazines;
        
        INSERT INTO authors (id, name) VALUES 
        (1, 'John Doe'),
        (2, 'Jane Smith');
        
        INSERT INTO magazines (id, name, category) VALUES 
        (1, 'Tech Today', 'Technology'),
        (2, 'Science Weekly', 'Science');
        
        INSERT INTO articles (id, title, author_id, magazine_id) VALUES 
        (1, 'The Future of AI', 1, 1),
        (2, 'Quantum Computing', 2, 1),
        (3, 'Genetic Engineering', 2, 2);
    """)
    conn.commit()
    conn.close()

def test_author_find_by_id():
    author = Author.find_by_id(1)
    assert author is not None
    assert author.name == "John Doe"
    assert author.id == 1

def test_author_articles():
    author = Author.find_by_id(1)
    articles = author.articles()
    assert len(articles) == 1
    assert articles[0].title == "The Future of AI"

def test_author_magazines():
    author = Author.find_by_id(2)
    magazines = author.magazines()
    assert len(magazines) == 2
    magazine_names = {m.name for m in magazines}
    assert "Tech Today" in magazine_names
    assert "Science Weekly" in magazine_names

def test_author_add_article():
    author = Author.find_by_id(1)
    magazine = Magazine.find_by_id(2)
    new_article = author.add_article(magazine, "New Article")
    
    assert new_article is not None
    assert new_article.title == "New Article"
    assert new_article.author_id == author.id
    assert new_article.magazine_id == magazine.id
    
  
    from_db = Article.find_by_id(new_article.id)
    assert from_db is not None
    assert from_db.title == "New Article"