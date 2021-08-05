from unittest import TestCase, main

from project.player.beginner import Beginner


class BeginnerTest(TestCase):
    def test_attrs_set_properly(self):
        beginner = Beginner("BeginnerName")
        self.assertEqual("BeginnerName", beginner.username)
        self.assertEqual(50, beginner.health)

    def test_player_username_is_empty_string_raises(self):
        with self.assertRaises(ValueError) as ex:
            player = Beginner("")
        self.assertEqual("Player's username cannot be an empty string.", str(ex.exception))

    def test_player_health_negative_value_raises(self):
        with self.assertRaises(ValueError) as ex:
            player = Beginner("Name")
            player.health = -5
        self.assertEqual("Player's health bonus cannot be less than zero.", str(ex.exception))

    def test_player_health_set_with_positive_value(self):
        player = Beginner("Name")
        player.health = 50
        self.assertEqual(50, player.health)

    def test_player_take_damage_negative_value_raises(self):
        with self.assertRaises(ValueError) as ex:
            player = Beginner("Name")
            player.take_damage(-5)
        self.assertEqual("Damage points cannot be less than zero.", str(ex.exception))

    def test_player_take_damage_set_with_positive_value(self):
        player = Beginner("Name")
        player.take_damage(45)
        self.assertEqual(5, player.health)

    def test_is_the_player_dead_when_health_is_les_than_zero(self):
        player = Beginner("Name")
        player.health = 0
        self.assertEqual(True, player.is_dead)

    def test_is_the_player_dead_when_health_positive_number(self):
        player = Beginner("Name")
        player.health = 300
        self.assertEqual(False, player.is_dead)


if __name__ == '__main__':
    main()