class Magazine:
    def __init__(self, id, name, category):
        self._id = None
        self._name = name
        self.category = category
    @staticmethod
    def validate_name(name):
        if not isinstance(name, str):
            raise ValueError("Name should be of type string")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 chars")
        return name
    def __repr__(self):
        return f'<Magazine {self.name}>'
