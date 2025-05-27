from lib.db.connection import get_connection
from lib.models.article import Article
from lib.models.author import Author

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    @classmethod
    def create(cls, name, category):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (name, category))
        conn.commit()
        return cls(cursor.lastrowid, name, category)

    @classmethod
    def get_all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines")
        return [cls(row["id"], row["name"], row["category"]) for row in cursor.fetchall()]

    def articles(self):
        return Article.find_by_magazine(self.id)

    def contributors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT a.* FROM authors a
            JOIN articles ar ON a.id = ar.author_id
            WHERE ar.magazine_id = ?
        """, (self.id,))
        return [Author(row["id"], row["name"]) for row in cursor.fetchall()]
