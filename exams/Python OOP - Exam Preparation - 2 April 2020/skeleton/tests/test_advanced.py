from unittest import TestCase, main

from project.player.advanced import Advanced


class AdvancedTest(TestCase):
    def test_attrs_set_properly(self):
        advanced = Advanced("AdvancedName")
        self.assertEqual("AdvancedName", advanced.username)
        self.assertEqual(250, advanced.health)

    def test_player_username_is_empty_string_raises(self):
        with self.assertRaises(ValueError) as ex:
            advanced = Advanced("")
        self.assertEqual("Player's username cannot be an empty string.", str(ex.exception))

    def test_player_health_negative_value_raises(self):
        with self.assertRaises(ValueError) as ex:
            player = Advanced("Name")
            player.health = -5
        self.assertEqual("Player's health bonus cannot be less than zero.", str(ex.exception))

    def test_player_health_set_with_positive_value(self):
        player = Advanced("Name")
        player.health = 50
        self.assertEqual(50, player.health)

    def test_player_take_damage_negative_value_raises(self):
        with self.assertRaises(ValueError) as ex:
            player = Advanced("Name")
            player.take_damage(-5)
        self.assertEqual("Damage points cannot be less than zero.", str(ex.exception))

    def test_player_take_damage_set_with_positive_value(self):
        player = Advanced("Name")
        player.take_damage(50)
        self.assertEqual(200, player.health)

    def test_is_the_player_dead_when_health_is_les_than_zero(self):
        player = Advanced("Name")
        player.health = 0
        self.assertEqual(True, player.is_dead)

    def test_is_the_player_dead_when_health_positive_number(self):
        player = Advanced("Name")
        player.health = 300
        self.assertEqual(False, player.is_dead)


if __name__ == '__main__':
    main()