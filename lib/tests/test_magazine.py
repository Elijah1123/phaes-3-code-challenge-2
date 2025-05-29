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
        (3, 'Bob Johnson'),
        (4, 'Alice Williams');
        
        INSERT INTO magazines (id, name, category) VALUES 
        (1, 'Tech Today', 'Technology'),
        (2, 'Science Weekly', 'Science'),
        (3, 'Business Insights', 'Business');
        
        INSERT INTO articles (id, title, author_id, magazine_id) VALUES 
        (1, 'The Future of AI', 1, 1),
        (2, 'Quantum Computing', 2, 1),
        (3, 'Neural Networks', 1, 1),
        (4, 'Genetic Engineering', 2, 2),
        (5, 'Market Trends 2023', 3, 3),
        (6, 'Startup Funding', 3, 3),
        (7, 'Blockchain Revolution', 3, 1),
        (8, 'New Battery Tech', 4, 1),
        (9, 'Space Exploration', 4, 2);
    """)
    conn.commit()
    conn.close()

def test_magazine_creation():
    """Test creating and saving a magazine"""
    magazine = Magazine("New Magazine", "General")
    magazine.save()
    
    assert magazine.id is not None
    assert magazine.name == "New Magazine"
    assert magazine.category == "General"

def test_magazine_find_by_id():
    """Test finding a magazine by ID"""
    magazine = Magazine.find_by_id(1)
    assert magazine is not None
    assert magazine.name == "Tech Today"
    assert magazine.category == "Technology"

def test_magazine_find_by_name():
    """Test finding a magazine by name"""
    magazine = Magazine.find_by_name("Science Weekly")
    assert magazine is not None
    assert magazine.id == 2
    assert magazine.category == "Science"

def test_magazine_articles():
    """Test getting all articles in a magazine"""
    magazine = Magazine.find_by_id(1)
    articles = magazine.articles()
    
    assert len(articles) == 4
    article_titles = {article.title for article in articles}
    expected_titles = {
        "The Future of AI",
        "Quantum Computing",
        "Neural Networks",
        "Blockchain Revolution"
    }
    assert article_titles == expected_titles

def test_magazine_contributors():
    """Test getting all unique contributors to a magazine"""
    magazine = Magazine.find_by_id(1)
    contributors = magazine.contributors()
    
    assert len(contributors) == 3
    contributor_names = {author.name for author in contributors}
    expected_names = {"John Doe", "Jane Smith", "Bob Johnson"}
    assert contributor_names == expected_names

def test_magazine_article_titles():
    """Test getting all article titles in a magazine"""
    magazine = Magazine.find_by_id(3)
    titles = magazine.article_titles()
    
    assert len(titles) == 2
    assert "Market Trends 2023" in titles
    assert "Startup Funding" in titles

def test_magazine_contributing_authors():
    """Test getting authors with more than 2 articles in a magazine"""
    # First add more articles to make Bob Johnson have 3 articles in Tech Today
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
        ("Another Tech Article", 3, 1)
    )
    conn.commit()
    conn.close()
    
    magazine = Magazine.find_by_id(1)
    contributors = magazine.contributing_authors()
    
    assert len(contributors) == 1
    assert contributors[0].name == "Bob Johnson"

def test_magazine_top_publisher():
    """Test finding the magazine with most articles"""
    top_magazine = Magazine.top_publisher()
    assert top_magazine is not None
    assert top_magazine.name == "Tech Today"
    assert top_magazine.category == "Technology"

def test_magazine_update():
    """Test updating a magazine"""
    magazine = Magazine.find_by_id(2)
    magazine.name = "Updated Science Weekly"
    magazine.category = "Updated Science"
    magazine.save()
    
    updated = Magazine.find_by_id(2)
    assert updated.name == "Updated Science Weekly"
    assert updated.category == "Updated Science"

def test_magazine_delete():
    """Test deleting a magazine"""
    magazine = Magazine.find_by_id(3)
    magazine.delete()
    
    deleted = Magazine.find_by_id(3)
    assert deleted is None
    
   
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM articles WHERE magazine_id = 3")
    articles = cursor.fetchall()
    conn.close()
    assert len(articles) == 0