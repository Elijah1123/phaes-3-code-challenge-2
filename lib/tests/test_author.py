import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import get_connection
from scripts.setup_db import setup_db

@pytest.fixture(autouse=True)
def reset_db():
    setup_db()
    conn = get_connection()
    cursor = conn.cursor()

    # Seed sample data
    cursor.execute("INSERT INTO authors (name) VALUES ('Jane Doe')")
    cursor.execute("INSERT INTO authors (name) VALUES ('John Smith')")

    cursor.execute("INSERT INTO magazines (name, category) VALUES ('Tech Weekly', 'Technology')")
    cursor.execute("INSERT INTO magazines (name, category) VALUES ('Health Digest', 'Health')")

    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('AI in 2025', 1, 1)")
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('Fitness Tips', 1, 2)")
    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('Quantum Computing', 2, 1)")

    conn.commit()
    yield
    conn.execute("DELETE FROM articles")
    conn.execute("DELETE FROM magazines")
    conn.execute("DELETE FROM authors")
    conn.commit()

def test_author_creation():
    author = Author.create("Alice")
    assert isinstance(author, Author)
    assert author.name == "Alice"

def test_get_all_authors():
    authors = Author.get_all()
    names = [a.name for a in authors]
    assert "Jane Doe" in names
    assert "John Smith" in names

def test_author_articles():
    author = Author(1, "Jane Doe")
    articles = author.articles()
    titles = [a.title for a in articles]
    assert "AI in 2025" in titles
    assert "Fitness Tips" in titles

def test_author_magazines():
    author = Author(1, "Jane Doe")
    magazines = author.magazines()
    mag_names = [m.name for m in magazines]
    assert "Tech Weekly" in mag_names
    assert "Health Digest" in mag_names
