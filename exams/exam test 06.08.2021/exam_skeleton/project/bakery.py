from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Name cannot be empty string or white space!")
        self._name = value

    def add_food(self, food_type: str, name: str, price: float):
        if food_type == "Bread":
            bread_names = [b.name for b in self.food_menu if b.__class__.__name__ == "Bread"]
            if name in bread_names:
                raise Exception(f"{food_type} {name} is already in the menu!")
            bread = Bread(name, price)
            self.food_menu.append(bread)
            return f"Added {name} ({food_type}) to the food menu"
        elif food_type == "Cake":
            cake_names = [c.name for c in self.food_menu if c.__class__.__name__ == "Cake"]
            if name in cake_names:
                raise Exception(f"{food_type} {name} is already in the menu!")
            cake = Cake(name, price)
            self.food_menu.append(cake)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: int, brand:str):
        if drink_type == "Water":
            water_names = [w.name for w in self.drinks_menu if w.__class__.__name__ == "Water"]
            if name in water_names:
                raise Exception(f"{drink_type} {name} is already in the menu!")
            water = Water(name, portion, brand)
            self.drinks_menu.append(water)
            return f"Added {name} ({brand}) to the drink menu"
        elif drink_type == "Tea":
            tea_names = [t.name for t in self.drinks_menu if t.__class__.__name__ == "Tea"]
            if name in tea_names:
                raise Exception(f"{drink_type} {name} is already in the menu!")
            tea = Tea(name, portion, brand)
            self.drinks_menu.append(tea)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type == "InsideTable":
            inside_table_numbers = [i.table_number for i in self.tables_repository if i.__class__.__name__ == "InsideTable"]
            if table_number in inside_table_numbers:
                raise Exception(f"Table {table_number} is already in the bakery!")
            inside_table = InsideTable(table_number, capacity)
            self.tables_repository.append(inside_table)
            return f"Added table number {table_number} in the bakery"
        elif table_type == "OutsideTable":
            outside_table_numbers = [i.table_number for i in self.tables_repository if i.__class__.__name__ == "OutsideTable"]
            if table_number in outside_table_numbers:
                raise Exception(f"Table {table_number} is already in the bakery!")
            outside_table = OutsideTable(table_number, capacity)
            self.tables_repository.append(outside_table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and number_of_people <= table.capacity:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names: str):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if not table:
            return f"Could not find table {table_number}"
        available_food = f"Table {table_number} ordered:\n"
        not_available_food = f"{self.name} does not have in the menu:\n"
        current_table = table[0]
        food_names_in_menu = [f.name for f in self.food_menu]
        for food_name in food_names:
            if food_name in food_names_in_menu:
                food = [f for f in self.food_menu if f.name == food_name][0]
                current_table.food_orders.append(food)
                available_food += f"{food}\n"
            else:
                not_available_food += f"{food_name}\n"
        result = available_food + not_available_food
        return result

    def order_drink(self, table_number: int, *drinks_names: str):
        table = [t for t in self.tables_repository if t.table_number == table_number]
        if not table:
            return f"Could not find table {table_number}"
        available_drink = f"Table {table_number} ordered:\n"
        not_available_drink = f"{self.name} does not have in the menu:\n"
        current_table = table[0]
        drink_names_in_menu = [f.name for f in self.drinks_menu]
        for drink_name in drinks_names:
            if drink_name in drink_names_in_menu:
                drink = [f for f in self.drinks_menu if f.name == drink_name][0]
                current_table.drink_orders.append(drink)
                available_drink += f"{drink}\n"
            else:
                not_available_drink += f"{drink_name}\n"
        result = available_drink + not_available_drink
        return result

    def leave_table(self, table_number: int):
        table = [t for t in self.tables_repository if t.table_number == table_number][0]
        result = f"Table: {table_number}\n"
        result += f"Bill: {table.get_bill():.2f}"
        self.total_income += table.get_bill()
        table.clear()
        return result

    def get_free_tables_info(self):
        result = ""
        for table in self.tables_repository:
            if not table.is_reserved:
                result += table.free_table_info() + '\n'
        return result

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
