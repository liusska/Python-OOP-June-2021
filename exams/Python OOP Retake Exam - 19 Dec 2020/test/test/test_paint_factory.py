from project.factory.paint_factory import PaintFactory

from unittest import TestCase, main


class PaintFactoryTests(TestCase):

    def test_attrs_set_properly(self):
        paint_factory = PaintFactory("Factory", 100)
        self.assertEqual("Factory", paint_factory.name)
        self.assertEqual(100, paint_factory.capacity)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], paint_factory.valid_ingredients)

    def test_add_ingredient(self):
        paint_factory = PaintFactory("Factory", 100)
        paint_factory.add_ingredient("yellow", 2)
        self.assertEqual(2, paint_factory.ingredients["yellow"])

    def test_add_ingredient_if_not_enough_capacity_raises(self):
        paint_factory = PaintFactory("Factory", 10)
        with self.assertRaises(ValueError) as ex:
            paint_factory.add_ingredient("yellow", 11)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_ingredient_if_not_in_allowed_ingredients_raises(self):
        paint_factory = PaintFactory("Factory", 100)
        with self.assertRaises(TypeError) as ex:
            paint_factory.add_ingredient("brown", 2)
        self.assertEqual("Ingredient of type brown not allowed in PaintFactory", str(ex.exception))

    def test_remove_ingredient(self):
        paint_factory = PaintFactory("Factory", 100)
        paint_factory.add_ingredient("yellow", 10)
        paint_factory.remove_ingredient("yellow", 5)
        self.assertEqual(5, paint_factory.ingredients["yellow"])

    def test_remove_ingredient_result_less_than_zero_raises(self):
        paint_factory = PaintFactory("Factory", 100)
        paint_factory.add_ingredient("yellow", 10)
        with self.assertRaises(ValueError) as ex:
            paint_factory.remove_ingredient("yellow", 11)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))


if __name__ == '__main__':
    main()