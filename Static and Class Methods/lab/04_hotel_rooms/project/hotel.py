class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [r for r in self.rooms if r.number == room_number][0]
        result = room.take_room(people)
        if not result:
            self.guests += people

    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number][0]
        self.guests -= room.guests
        room.free_room()

    def status(self):
        free_rooms = [x for x in self.rooms if not x.is_taken]
        taken_rooms = [x for x in self.rooms if x.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join([str(x.number) for x in free_rooms])}\n" \
               f"Taken rooms: {', '.join([str(x.number) for x in taken_rooms])}"


