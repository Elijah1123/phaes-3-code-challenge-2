from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article


authors = [
    Author(name="Elijah Mzaleno"),
    Author(name="Jane Doe"),
    Author(name="John Smith")
]
for author in authors:
    author.save()


magazines = [
    Magazine(name="Global Science", category="Science"),
    Magazine(name="Modern Tech", category="Technology"),
    Magazine(name="Health Digest", category="Health")
]
for magazine in magazines:
    magazine.save()


articles = [
    Article(title="Quantum Realms", author_id=authors[0].id, magazine_id=magazines[0].id),
    Article(title="AI Revolution", author_id=authors[1].id, magazine_id=magazines[1].id),
    Article(title="Nutrition Basics", author_id=authors[2].id, magazine_id=magazines[2].id),
    Article(title="Space Exploration", author_id=authors[0].id, magazine_id=magazines[0].id)
]
for article in articles:
    article.save()

print("Database seeded successfully.")
