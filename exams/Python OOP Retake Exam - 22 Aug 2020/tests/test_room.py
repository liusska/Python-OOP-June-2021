from project.rooms.room import Room

from unittest import TestCase, main


class TestCaseBase(TestCase):
    def assertListEmpty(self, ll):
        self.assertListEqual([], ll)


class RoomTests(TestCaseBase):
    def test__init__when_all_valid__should_be_set(self):
        name = "RoomName"
        budget = 123
        members_count = 4
        room = Room(name, budget, members_count)
        self.assertEqual(name, room.family_name)
        self.assertEqual(budget, room.budget)
        self.assertEqual(members_count, room.members_count)
        self.assertEqual(0, room.expenses)
        self.assertListEmpty(room.children)

    def test__expenses_when_is_positive_expect_to_set(self):
        name = "RoomName"
        budget = 123
        members_count = 4
        room = Room(name, budget, members_count)
        room.expenses = 5
        self.assertEqual(5, room.expenses)

    def test__expenses_is_0_expect_raise(self):
        name = "RoomName"
        budget = 123
        members_count = 4
        room = Room(name, budget, members_count)
        room.expenses = 0
        self.assertEqual(0, room.expenses)

    def test__expenses_is_negative_expect_raise(self):
        name = "RoomName"
        budget = 123
        members_count = 4
        room = Room(name, budget, members_count)
        with self.assertRaises(ValueError) as ex:
            room.expenses = -123
        self.assertEqual("Expenses cannot be negative", str(ex.exception))



if __name__ == '__main__':
    main()