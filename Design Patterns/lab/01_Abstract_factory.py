from abc import ABC, abstractmethod


class Chair:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Sofa:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Table:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self):
        pass

    @abstractmethod
    def create_sofa(self):
        pass

    @abstractmethod
    def create_table(self):
        pass


class VictorianFactory(AbstractFactory):
    def create_chair(self):
        return Chair('Victorian chair')

    def create_sofa(self):
        return Sofa('Victorian sofa')

    def create_table(self):
        return Table('Victorian table')


class ArtFactory(AbstractFactory):
    def create_chair(self):
        return Chair('Art chair')

    def create_sofa(self):
        return Sofa('Art sofa')

    def create_table(self):
        return Table('Art table')


class ModernFactory(AbstractFactory):
    def create_chair(self):
        return Chair('Modern chair')

    def create_sofa(self):
        return Sofa('Modern sofa')

    def create_table(self):
        return Table('Modern table')


class FuturisticFactory(AbstractFactory):
    def create_chair(self):
        return Chair('Futuristic chair')

    def create_sofa(self):
        return Sofa('Futuristic sofa')

    def create_table(self):
        return Table('Futuristic table')


def get_factory(style):
    if style == "Victorian":
        return VictorianFactory()
    elif style == "Modern":
        return ModernFactory()
    elif style == "Art":
        return ArtFactory()
    elif style == "Futuristic":
        return FuturisticFactory()


if __name__ == '__main__':
    client_style = input()
    factory = get_factory(client_style)
    print(factory.create_chair())
