from unittest import TestCase, main

from project.card.magic_card import MagicCard


class MagicCardTests(TestCase):
    def test_attrs_set_properly(self):
        magic_card = MagicCard("Magic")
        self.assertEqual("Magic", magic_card.name)
        self.assertEqual(5, magic_card.damage_points)
        self.assertEqual(80, magic_card.health_points)

    def test_name_is_empty_string_raises(self):
        with self.assertRaises(ValueError) as ex:
            card = MagicCard("")
        self.assertEqual("Card's name cannot be an empty string.", str(ex.exception))

    def test_name_is_correctly_set(self):
        card = MagicCard("MagicCard")
        self.assertEqual("MagicCard", card.name)

    def test_card_with_negative_damage_points_raises(self):
        with self.assertRaises(ValueError) as ex:
            card = MagicCard("NewCard")
            card.damage_points = -20
        self.assertEqual("Card's damage points cannot be less than zero.", str(ex.exception))

    def test_card_with_positive_damage_points(self):
        card = MagicCard("NewCard")
        card.damage_points = 20
        self.assertEqual(20, card.damage_points)

    def test_card_with_negative_health_points_raises(self):
        with self.assertRaises(ValueError) as ex:
            card = MagicCard("NewCard")
            card.health_points = -20
        self.assertEqual("Card's HP cannot be less than zero.", str(ex.exception))

    def test_card_with_positive_health_points(self):
        card = MagicCard("NewCard")
        card.health_points = 20
        self.assertEqual(20, card.health_points)


if __name__ == '__main__':
    main()