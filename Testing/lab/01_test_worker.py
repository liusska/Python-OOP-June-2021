class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Test", 100, 10)

    def test_person_is_initialised_correctly(self):
        # Assert
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(100, self.worker.salary)
        self.assertEqual(10, self.worker.energy)

    def test_worker_energy_increased_after_rest(self):
        self.assertEqual(10, self.worker.energy)
        self.worker.rest()
        self.assertEqual(11, self.worker.energy)

    def test_worker_works_with_negative_energy_raises(self):
        worker = Worker("Test", 100, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_money_is_increased_after_work(self):
        self.worker.work()
        self.worker.work()
        self.assertEqual(200, self.worker.money)
        # self.assertEqual(8, self.worker.energy)

    def test_worker_energy_is_decreased_after_work(self):
        self.worker.work()
        self.assertEqual(9, self.worker.energy)

    def test_get_info(self):
        worker = Worker("Test", 100, 10)
        actual_result = worker.get_info()
        expected_result = f'Test has saved 0 money.'
        self.assertEqual(actual_result, expected_result)



if __name__ == '__main__':
    unittest.main()

