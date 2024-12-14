from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def id(self):
        return self.id
    @property
    def name(self):
        return self._name
    @staticmethod
    def validate_name(name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non empty string.")
        return name
    def save(self):
        return self
    pass
    def articles(self):
        return cursor.fetchall()
    def magazines(self):
        return cursor.fetchall()
    @classmethod
    def drop_table(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS authors')
        conn.commit()
        conn.close()
    # def __repr__(self):
    #     return f'<Author {self.name}>'
    
