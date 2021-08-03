from project.vehicle import Vehicle

from unittest import TestCase, main


class VehicleTests(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(fuel=10, horse_power=100)

    def test_init(self):
        self.assertEqual(10, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_with_less_fuel_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive(self):
        self.vehicle.drive(2)
        self.assertEqual(7.5, self.vehicle.fuel)

    def test_refuel_not_enough_capacity(self):
        self.vehicle.capacity = 100
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(100)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel(self):
        self.vehicle.capacity = 100
        self.vehicle.refuel(50)
        self.assertEqual(60, self.vehicle.fuel)

    def test_info(self):
        actual_result = self.vehicle.__str__()
        expected_result = f"The vehicle has {self.vehicle.horse_power} horse power with {self.vehicle.fuel}" \
                          f" fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    main()