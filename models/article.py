from database.connection import get_db_connection
from models.author import Author
from models.magazine import Magazine


class Article:
    def __init__(self, title, content, author, magazine):
        self._id = None
        self._title = self.validate_title(title)
        self._content = content  # No need for validation if just a string
        self._author = author
        self._magazine = magazine
        self.save()

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def content(self):
        return self._content

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO articles (title, content, author_id, magazine_id) 
            VALUES (?, ?, ?, ?)
        ''', (self._title, self._content, self._author.id, self._magazine.id))
        conn.commit()
        self._id = cursor.lastrowid

    @staticmethod
    def validate_title(title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        return title

    @classmethod
    def drop_table(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS articles')
        conn.commit()
