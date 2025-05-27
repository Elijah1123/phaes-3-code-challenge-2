from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article


if __name__ == '__main__':
    
    author = Author(name="Alice")
    author.save()

    magazine = Magazine(name="Science Daily", category="Science")
    magazine.save()

    article = Article(title="New Discoveries", author_id=author.id, magazine_id=magazine.id)
    article.save()

    # Fetch data
    print("Author's Articles:", author.articles())
    print("Author's Magazines:", author.magazines())
    print("Magazine's Articles:", magazine.articles())
    print("Magazine Contributors:", magazine.contributors())