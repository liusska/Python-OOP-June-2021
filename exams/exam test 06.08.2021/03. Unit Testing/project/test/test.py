from project.pet_shop import PetShop

from unittest import TestCase, main


class PetShopTests(TestCase):
    def setUp(self):
        self.shop = PetShop("Shop")

    def test_attrs_set(self):
        self.assertEqual("Shop", self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

    def test_add_food_with_negative_quantity_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.shop.add_food("bread", -5)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_in_existing_food_type_with_positive_quantity(self):
        self.shop.food = {'meat': 10}
        result = self.shop.add_food('meat', 10)
        self.assertEqual(20, self.shop.food['meat'])
        self.assertEqual(f"Successfully added 10.00 grams of meat.", result)

    def test_add_food_in_not_existing_food_type(self):
        result = self.shop.add_food('meat', 10)
        self.assertEqual(10, self.shop.food['meat'])
        self.assertEqual(f"Successfully added 10.00 grams of meat.", result)

    def test_add_pet_if_is_already_existing_in_list_raises(self):
        self.shop.pets = ["Lilly", "Tom"]
        with self.assertRaises(Exception) as ex:
            self.shop.add_pet("Tom")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet_successfully(self):
        result = self.shop.add_pet("Johny")
        self.assertEqual(["Johny"], self.shop.pets)
        self.assertEqual(1, len(self.shop.pets))
        self.assertEqual("Successfully added Johny.", result)

    def test_feed_not_existing_pet_raises(self):
        self.shop.food = {'meat': 10}
        self.shop.pets = ['Tom']
        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet('meat', 'Lilly')
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feet_pet_with_not_existing_food_type_message(self):
        self.shop.food = {'meat': 10}
        self.shop.pets = ['Tom']
        message = self.shop.feed_pet('hamburger', 'Tom')
        self.assertEqual({'meat': 10}, self.shop.food)
        self.assertEqual(['Tom'], self.shop.pets)
        self.assertEqual('You do not have hamburger', message)

    def test_feed_pet_if_food_is_les_than_100_message(self):
        self.shop.food = {'meat': 10}
        self.shop.pets = ['Tom']
        result = self.shop.feed_pet('meat', 'Tom')
        self.assertEqual(1010.00, self.shop.food['meat'])
        self.assertEqual("Adding food...", result)

    def test_feed_pet_message(self):
        self.shop.food = {'meat': 110}
        self.shop.pets = ['Tom']
        result = self.shop.feed_pet('meat', 'Tom')
        self.assertEqual(10, self.shop.food['meat'])
        self.assertEqual(['Tom'], self.shop.pets)
        self.assertEqual("Tom was successfully fed", result)

    def test_represent_pets_message(self):
        self.shop.pets = ['Tom', 'Lilly', 'John']
        expected_result = f'Shop {self.shop.name}:\nPets: {", ".join(self.shop.pets)}'
        actual_result = self.shop.__repr__()
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    main()