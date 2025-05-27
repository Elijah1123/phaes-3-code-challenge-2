from lib.db.connection import get_connection

class Article:
    def __init__(self, id, title, author_id, magazine_id):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    @classmethod
    def create(cls, title, author_id, magazine_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", (title, author_id, magazine_id))
        conn.commit()
        return cls(cursor.lastrowid, title, author_id, magazine_id)

    @classmethod
    def get_all(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles")
        return [cls(row["id"], row["title"], row["author_id"], row["magazine_id"]) for row in cursor.fetchall()]

    @classmethod
    def find_by_author(cls, author_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (author_id,))
        return [cls(row["id"], row["title"], row["author_id"], row["magazine_id"]) for row in cursor.fetchall()]

    @classmethod
    def find_by_magazine(cls, magazine_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id = ?", (magazine_id,))
        return [cls(row["id"], row["title"], row["author_id"], row["magazine_id"]) for row in cursor.fetchall()]
