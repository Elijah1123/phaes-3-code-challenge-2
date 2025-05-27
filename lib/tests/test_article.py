import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

@pytest.fixture
def setup_entities():
    author = Author(name="Test Author")
    author.save()
    magazine = Magazine(name="Tech Mag", category="Technology")
    magazine.save()
    return author, magazine

def test_create_article(setup_entities):
    author, magazine = setup_entities
    article = Article(title="Tech Innovations", author_id=author.id, magazine_id=magazine.id)
    article.save()
    assert article.id is not None

def test_find_by_id(setup_entities):
    author, magazine = setup_entities
    article = Article(title="AI Advances", author_id=author.id, magazine_id=magazine.id)
    article.save()
    found = Article.find_by_id(article.id)
    assert found.title == "AI Advances"

def test_find_by_title(setup_entities):
    author, magazine = setup_entities
    article = Article(title="Quantum Computing", author_id=author.id, magazine_id=magazine.id)
    article.save()
    found = Article.find_by_title("Quantum Computing")
    assert found.magazine_id == magazine.id

def test_find_by_author(setup_entities):
    author, magazine = setup_entities
    article = Article(title="Cybersecurity", author_id=author.id, magazine_id=magazine.id)
    article.save()
    results = Article.find_by_author(author.id)
    assert any(a.title == "Cybersecurity" for a in results)

def test_find_by_magazine(setup_entities):
    author, magazine = setup_entities
    article = Article(title="Networking", author_id=author.id, magazine_id=magazine.id)
    article.save()
    results = Article.find_by_magazine(magazine.id)
    assert any(a.title == "Networking" for a in results)
