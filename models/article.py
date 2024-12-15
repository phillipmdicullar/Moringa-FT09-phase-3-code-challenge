class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self._id = id
        self._title = title
        self._content = content
        self._author_id = author_id
        self._magazine_id = magazine_id
        self.save() #
    def __repr__(self):
        return f'<Article {self.title}>'
    @staticmethod
    def validate_title(title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        return title
    @classmethod
    def create_table(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF EXISTS articles(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            FOREIGN KEY(author_id) REFERENCES authors(id),
            FOREIGN KEY(magazine_id) REFERENCES magazines(id))''')
        conn.commit()
    def save(self):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)''',(self._title, self._content, self._author.id, self._magazine.id))
            self._id = cursor.lastrowid