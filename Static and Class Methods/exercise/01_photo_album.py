class PhotoAlbum:

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for num in range(self.pages)]
        self.page = 0

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(photos_count//4)

    def add_photo(self, label: str):
        try:
            if len(self.photos[self.page]) == 4:
                self.page += 1
        except:
            return "No more free slots"

        if self.page >= self.pages:
            return "No more free slots"
        self.photos[self.page].append(label)
        return f"{label} photo added successfully on page {self.page + 1} slot {len(self.photos[self.page])}"

    def display(self):
        result = ""
        for page in self.photos:
            result += '-'*11 + '\n'
            for index in range(len(page)):
                if index == len(page) - 1:
                    result += "[]"
                else:
                    result += "[] "
            result += '\n'
        result += '-' * 11 + '\n'
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
