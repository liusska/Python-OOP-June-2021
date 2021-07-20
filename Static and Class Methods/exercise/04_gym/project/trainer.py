class Trainer:
    _id = 0

    def __init__(self, name):
        self.name = name
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        Trainer._id += 1
        return Trainer._id

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"