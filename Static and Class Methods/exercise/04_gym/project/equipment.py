class Equipment:
    _id = 0

    def __init__(self, name):
        self.name = name
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        Equipment._id += 1
        return Equipment._id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"