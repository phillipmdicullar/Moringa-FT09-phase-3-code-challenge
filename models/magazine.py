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
#implement contributors method to fetch distinct authors for a a magazine
    def contributors(self):
        from models.author import Author
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''SELECT DISTINCT authors.id, authors.name FROM authors JOIN articles ON authors.id = articles.author_id WHERE articles.magazine_id = ?''', (self.id,))
        rows = cursor.fetchall()
        return [Author(row["id"], row["name"]) for row in rows]
    def contributing_authors(self):
        from models.author import Author
        articles = self.articles()
        if not articles:
            return None
        author_counts = {}
        for article in articles:
            author_counts[article.author_id] = author_counts.get(article.author_id, 0) + 1
        contributing_authors = [Author.find_by_id(author_id) for author_id, count in author_counts.items() if count > 2 ]
        return contributing_authors if contributing_authors else None
    