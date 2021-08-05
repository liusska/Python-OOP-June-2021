from unittest import TestCase, main

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard


class CardRepositoryTests(TestCase):
    def setUp(self):
        self.repo = CardRepository()
        self.magic = MagicCard("Magic")
        self.trap = TrapCard("Trap")
        self.repo.count = 2
        self.repo.cards = [self.magic, self.trap]

    def test_attrs_set(self):
        self.assertEqual(2, self.repo.count)
        self.assertEqual([self.magic, self.trap], self.repo.cards)

    def test_add_card_successfully(self):
        new_card = MagicCard("NewMagic")
        self.repo.add(new_card)
        self.assertEqual(3, len(self.repo.cards))
        self.assertEqual(3, self.repo.count)

    def test_add_existing_card_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.repo.add(self.magic)
        self.assertEqual(f"Card {self.magic.name} already exists!", str(ex.exception))

    def test_remove_card_successfully(self):
        self.repo.remove("Trap")
        self.assertEqual(1, self.repo.count)
        self.assertEqual(1, len(self.repo.cards))
        self.assertEqual([self.magic], self.repo.cards)

    def test_remove_card_with_empty_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.repo.remove("")
        self.assertEqual("Card cannot be an empty string!", str(ex.exception))

    def test_find_card(self):
        result = self.repo.find("Magic")
        self.assertEqual(self.magic, result)


if __name__ == '__main__':
    main()