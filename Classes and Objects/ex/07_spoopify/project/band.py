
class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        album_to_remove = [album for album in self.albums if album_name == album.name]
        if album_to_remove:
            if album_to_remove[0].published:
                return "Album has been published. It cannot be removed."
            self.albums.remove(album_to_remove[0])
            return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}\n"
        for album in self.albums:
            result += f"{album.details()}"
        return result
