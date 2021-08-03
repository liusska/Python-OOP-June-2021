from project.hardware.hardware import Hardware
from project.software.software import Software

from unittest import TestCase, main


class HardwareTests(TestCase):

    def test_init_set_correctly_heavy_hardware(self):
        hardware = Hardware("Name", "Heavy", 100, 100)
        self.assertEqual("Name", hardware.name)
        self.assertEqual("Heavy", hardware.type)
        self.assertEqual(100, hardware.capacity)
        self.assertEqual(100, hardware.memory)
        self.assertEqual([], hardware.software_components)

    def test_install_software_if_enough_memory_and_capacity(self):
        software = Software("Name", "Light", 10, 10)
        hardware = Hardware("Name", "Heavy", 100, 100)
        hardware.install(software)
        self.assertEqual([software], hardware.software_components)

    def test_install_software_not_enough_capacity_memory_raises(self):
        software = Software("Name", "Light", 10, 10)
        hardware = Hardware("Name", "Heavy", 2, 5)
        with self.assertRaises(Exception) as ex:
            hardware.install(software)
        self.assertEqual("Software cannot be installed", str(ex.exception))

    def test_uninstall_software(self):
        hardware = Hardware("Name", "Heavy", 100, 100)
        software = Software("Name", "Light", 10, 10)
        hardware.install(software)
        hardware.uninstall(software)
        self.assertEqual([], hardware.software_components)



if __name__ == '__main__':
    main()