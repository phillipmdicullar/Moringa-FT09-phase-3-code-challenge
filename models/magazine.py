class Magazine:
    def __init__(self, id, name, category):
        self._id = None
        self._name = self.validate_name(name)
        self.category = self.validate_category(category)
    def article_titles(self):
        #articles associated woith the magazine 
        all_articles = self.articles()
        if not all_articles:
            return None
        #get article titles
        titles = [article.title for article in articles]
        return titles
        pass
    @staticmethod
    def validate_name(name):
        if not isinstance(name, str):
            raise ValueError("Name should be of type string")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 chars")
        return name
    @staticmethod
    def validate_category(category):
        if not isinstance(category, str):
            raise ValueError("Category must be a string")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        return category
    def __repr__(self):
        return f'<Magazine {self.name}>'
