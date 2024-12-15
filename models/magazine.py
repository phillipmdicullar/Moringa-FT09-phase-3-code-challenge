from database.connection import get_db_connection

class Magazine:
    def __init__(self, name, category):
        self._id = None
        self._name = self.validate_name(name)
        self._category = self.validate_category(category)
        self.save()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def save(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (self._name, self._category))
        conn.commit()
        self._id = cursor.lastrowid

    @staticmethod
    def validate_name(name):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        return name

    @staticmethod
    def validate_category(category):
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        return category
#implement article methods to fetch all articles related to the magazine
    def articles(self):
        from models.article import Article
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''SELECT articles.id, articles.title,articles.content, articles.author_id,articles.magazine_id FROM articles WHERE articles.magazine_id= ?''', (self.id,))
        rows = cursor.fetchall()
        return [Article(row["id"], row["title"], row["content"], row["author_id"], self) for row in rows ]
