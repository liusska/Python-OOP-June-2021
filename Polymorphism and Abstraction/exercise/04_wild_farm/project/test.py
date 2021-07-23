# first zero test
import unittest
from wild_farm_04.project.animals.birds import Owl, Hen
from wild_farm_04.project.animals.mammals import Mouse, Dog, Cat, Tiger
from wild_farm_04.project.food import Vegetable, Fruit, Meat, Seed

hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)

