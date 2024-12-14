import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine

class TestModels(unittest.TestCase):
    def test_author_creation(self):
        author = Author("John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        article = Article(1, "Test Title", "Test Content", 1, 1)
        magazine = Magazine("Tech Weekly", "Technology")
        author = Author("John Doe")
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine(1, "Tech Weekly")
        self.assertEqual(magazine.name, "Tech Weekly")
    def test_author_name_change(self):
        author = Author("John Doe")
        with self.assertRaises(AttributeError):
            author.name = "Jane Doe"
    def test_author_name_type(self):
        with self.assertRaises(ValueError):
            author = Author(123)
    def test_author_name_length(self):
        with self.assertRaises(ValueError):
            author = Author("")
    def test_author_magazines(self):
        author = Author("John Doe")
        magazines = author.magazines()
        self.assertEqual(len(magazines), 0)
    def test_author_articles(self):
        author = Author("John Doe")
        articles = author.articles()
        self.assertEqual(len(articles), 0) 
  
if __name__ == "__main__":
    unittest.main()
