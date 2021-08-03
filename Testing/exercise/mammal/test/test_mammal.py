from project.mammal import Mammal

from unittest import TestCase, main


class MammalTests(TestCase):
    def setUp(self):
        self.mammal = Mammal("Tom", "cat", "Meow")

    def test_init(self):
        self.assertEqual("Tom", self.mammal.name)
        self.assertEqual("cat", self.mammal.type)
        self.assertEqual("Meow", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        actual_result = self.mammal.make_sound()
        expected_result = f"{self.mammal.name} makes {self.mammal.sound}"
        self.assertEqual(actual_result, expected_result)

    def test_get_kingdom(self):
        actual_result = self.mammal.get_kingdom()
        expected_result = "animals"
        self.assertEqual(expected_result, actual_result)

    def test_get_result(self):
        actual_result = self.mammal.info()
        expected_result = f"{self.mammal.name} is of type {self.mammal.type}"
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    main()
