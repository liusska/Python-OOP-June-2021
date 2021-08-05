from unittest import TestCase, main

from project.card.trap_card import TrapCard


class TrapCardTests(TestCase):
    def test_attrs_set_properly(self):
        trap_card = TrapCard("Trap")
        self.assertEqual("Trap", trap_card.name)
        self.assertEqual(120, trap_card.damage_points)
        self.assertEqual(5, trap_card.health_points)

    def test_name_is_empty_string_raises(self):
        with self.assertRaises(ValueError) as ex:
            card = TrapCard("")
        self.assertEqual("Card's name cannot be an empty string.", str(ex.exception))

    def test_name_is_correctly_set(self):
        card = TrapCard("TrapCard")
        self.assertEqual("TrapCard", card.name)

    def test_card_with_negative_damage_points_raises(self):
        with self.assertRaises(ValueError) as ex:
            card = TrapCard("NewCard")
            card.damage_points = -20
        self.assertEqual("Card's damage points cannot be less than zero.", str(ex.exception))

    def test_card_with_positive_damage_points(self):
        card = TrapCard("NewCard")
        card.damage_points = 20
        self.assertEqual(20, card.damage_points)

    def test_card_with_negative_health_points_raises(self):
        with self.assertRaises(ValueError) as ex:
            card = TrapCard("NewCard")
            card.health_points = -20
        self.assertEqual("Card's HP cannot be less than zero.", str(ex.exception))

    def test_card_with_positive_health_points(self):
        card = TrapCard("NewCard")
        card.health_points = 20
        self.assertEqual(20, card.health_points)





if __name__ == '__main__':
    main()