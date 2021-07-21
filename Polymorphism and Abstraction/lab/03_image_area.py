class ImageArea:
    def __init__(self, width, height):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()


)


