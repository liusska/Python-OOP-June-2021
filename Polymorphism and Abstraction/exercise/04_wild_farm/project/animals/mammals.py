from project.animals.animal import Mammal


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if not food.__class__.__name__ == "Vegetable" and not food.__class__.__name__ == "Fruit":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.10 * food.quantity
        self.food_eaten += food.quantity


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if not food.__class__.__name__ == "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.40 * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if not food.__class__.__name__ == "Meat" and not food.__class__.__name__ == "Vegetable":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.30 * food.quantity
        self.food_eaten += food.quantity


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if not food.__class__.__name__ == "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 1.00 * food.quantity
        self.food_eaten += food.quantity
