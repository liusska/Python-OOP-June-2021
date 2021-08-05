from unittest import TestCase, main

from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class PlayerRepositoryTests(TestCase):
    def setUp(self):
        self.repo = PlayerRepository()
        self.beginner = Beginner("Beginner")
        self.advanced = Advanced("Advanced")
        self.repo.count = 2
        self.repo.players = [self.beginner, self.advanced]

    def test_attrs_set(self):
        self.assertEqual(2, self.repo.count)
        self.assertEqual([self.beginner, self.advanced], self.repo.players)

    def test_add_player_successfully(self):
        new_player = Beginner("NewBeginner")
        self.repo.add(new_player)
        self.assertEqual(3, len(self.repo.players))
        self.assertEqual(3, self.repo.count)

    def test_add_existing_player_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.repo.add(self.beginner)
        self.assertEqual(f"Player {self.beginner.username} already exists!", str(ex.exception))

    def test_remove_player_successfully(self):
        self.repo.remove("Beginner")
        self.assertEqual(1, self.repo.count)
        self.assertEqual(1, len(self.repo.players))
        self.assertEqual([self.advanced], self.repo.players)

    def test_remove_card_with_empty_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.repo.remove("")
        self.assertEqual("Player cannot be an empty string!", str(ex.exception))

    def test_find_card(self):
        result = self.repo.find("Beginner")
        self.assertEqual(self.beginner, result)


if __name__ == '__main__':
    main()