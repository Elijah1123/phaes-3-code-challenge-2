import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

@pytest.fixture
def setup_magazine():
    magazine = Magazine(name="World News", category="Politics")
    magazine.save()
    return magazine

def test_create_magazine():
    magazine = Magazine(name="Health Weekly", category="Health")
    magazine.save()
    assert magazine.id is not None

def test_find_by_id(setup_magazine):
    found = Magazine.find_by_id(setup_magazine.id)
    assert found.name == "World News"

def test_find_by_name():
    magazine = Magazine(name="Eco Today", category="Environment")
    magazine.save()
    found = Magazine.find_by_name("Eco Today")
    assert found.category == "Environment"

def test_find_by_category():
    magazine = Magazine(name="Digital Age", category="Technology")
    magazine.save()
    found = Magazine.find_by_category("Technology")
    assert found.name == "Digital Age"

def test_articles_and_contributors():
    author = Author(name="Tech Guru")
    author.save()
    magazine = Magazine(name="AI Monthly", category="Tech")
    magazine.save()
    article1 = Article(title="AI and You", author_id=author.id, magazine_id=magazine.id)
    article1.save()
    article2 = Article(title="Machine Learning Basics", author_id=author.id, magazine_id=magazine.id)
    article2.save()

    assert len(magazine.articles()) == 2
    assert author in magazine.contributors()
    assert magazine.article_titles() == ["AI and You", "Machine Learning Basics"]
    assert author in magazine.contributing_authors()
