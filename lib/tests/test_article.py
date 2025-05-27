import pytest
from lib.models.article import Article
from lib.db.connection import get_connection
from scripts.setup_db import setup_db

@pytest.fixture(autouse=True)
def reset_db():
    setup_db()
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM magazines")
    cursor.execute("DELETE FROM authors")
    conn.commit()

    cursor.execute("INSERT INTO authors (name) VALUES ('Jane Doe')")
    cursor.execute("INSERT INTO magazines (name, category) VALUES ('Tech Weekly', 'Technology')")

    cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES ('AI in 2025', 1, 1)")
    conn.commit()
    yield

    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM magazines")
    cursor.execute("DELETE FROM authors")
    conn.commit()

def test_article_creation():
    article = Article.create("New Article", 1, 1)
    assert article.title == "New Article"
    assert article.author_id == 1
    assert article.magazine_id == 1

def test_find_by_author():
    articles = Article.find_by_author(1)
    titles = [a.title for a in articles]
    assert "AI in 2025" in titles
