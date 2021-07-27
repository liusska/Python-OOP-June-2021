class Bunker:
    survivors = []
    supplies = []
    medicine = []

    @property
    def food(self):
        food_obj = [s for s in self.supplies if s.__class__.__name__ == "FoodSupply"]
        if food_obj:
            return food_obj
        raise IndexError("There are no food supplies left!")

    @property
    def water(self):
        water_obj = [s for s in self.supplies if s.__class__.__name__ == "WaterSupply"]
        if water_obj:
            return water_obj
        raise IndexError("There are no water supplies left!")

    @property
    def painkillers(self):
        painkillers_obj = [m for m in self.medicine if m.__class__.__name__ == "Painkiller"]
        if painkillers_obj:
            return painkillers_obj
        raise IndexError("There are no painkillers left!")

    @property
    def salves(self):
        salve_obj = [m for m in self.medicine if m.__class__.__name__ == "Salve"]
        if salve_obj:
            return salve_obj
        raise IndexError("There are no salves left!")

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f"Survivor with name {survivor.name} already exists.")
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type: str):
        medicines = [m for m in self.medicine if m.__class__.__name__ == medicine_type]
        if medicines and survivor.needs_healing:
            current = medicines.pop()
            current.apply(survivor)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type: str):
        current_supplies = [m for m in self.supplies if m.__class__.__name__ == sustenance_type]
        if current_supplies and survivor.needs_sustenance:
            current = current_supplies.pop()
            current.apply(survivor)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        pass
        # for survivor in self.survivors:
        #     survivor.needs -= survivor.age * 2
        #     food = self.food
        #     water = self.water
        #     if food:
        #         self.supplies.remove(food[0])
        #     if water:
        #         self.supplies.remove(water[0])
