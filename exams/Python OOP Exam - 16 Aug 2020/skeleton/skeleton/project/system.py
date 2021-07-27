from project.hardware.power_hardware import PowerHardware
from project.hardware.heavy_hardware import HeavyHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def register_light_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = LightSoftware(name, capacity_consumption, memory_consumption)
            hardware.install(software)
            System._software.append(software)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name:str, software_name:str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [s for s in System._software if s.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        capacity_used = sum([h.used_capacity for h in System._hardware])
        memory_used = sum([h.used_memory for h in System._hardware])
        total_capacity = sum([c.capacity for c in System._hardware])
        total_memory = sum([m.memory for m in System._hardware])
        return f"System Analysis\nHardware Components: {len(System._hardware)}\n" \
               f"Software Components: {len(System._software)}\n" \
               f"Total Operational Memory: {memory_used} / {total_memory}\n" \
               f"Total Capacity Taken: {capacity_used} / {total_capacity}"

    @staticmethod
    def system_split():
        result = ""
        for h in System._hardware:
            result += f"Hardware Component - {h.name}\n"
            express_software = [s for s in h.software_components if s.type == "Express"]
            result += f"Express Software Components: {len(express_software)}\n"
            light_software = [s for s in h.software_components if s.type == "Light"]
            result += f"Light Software Components: {len(light_software)}\n"

            total_memory_used = sum([s.memory_consumption for s in h.software_components])
            result += f"Memory Usage: {total_memory_used} / {h.memory}\n"

            total_capacity_used = sum([s.capacity_consumption for s in h.software_components])
            result += f"Capacity Usage: {total_capacity_used} / {h.capacity}\n"

            result += f"Type: {h.type}\n"

            names = ', '.join([s.name for s in h.software_components])
            result += f"Software Components: {names if names else None}"

        return result