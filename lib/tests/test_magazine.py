import pytest
from lib.models.magazine import Magazine
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

def test_magazine_creation():
    magazine = Magazine.create("Health Monthly", "Health")
    assert magazine.name == "Health Monthly"
    assert magazine.category == "Health"

def test_find_by_name():
    magazine = Magazine.find_by_name("Tech Weekly")
    assert magazine is not None
    assert magazine.name == "Tech Weekly"

def test_get_all_magazines():
    magazines = Magazine.get_all()
    names = [m.name for m in magazines]
    assert "Tech Weekly" in names
