from copy import deepcopy

class CustomList:
    def __init__(self, *args):
        self.__values = list(args)

    def append(self, value):
        self.__values.append(value)

    def remove(self, index):
        try:
            return self.__values.pop(index)
        except IndexError:
            raise IndexError("Invalid index")

    def get(self, index):
        try:
            return self.__values[index]
        except IndexError:
            raise IndexError("Invalid index")

    def extend(self, obj):
        try:
            iter(obj)
            self.__values.extend(obj)
        except TypeError:
            self.__values.append(obj)
        return deepcopy(self.__values)

    def insert(self, index, value):
        if index >= len(self.__values) or index < 0:
            raise IndexError("Invalid index")
        self.__values.insert(index, value)
        return self.__values

    def pop(self):
        try:
            return self.__values.pop()
        except IndexError:
            raise IndexError("No elements in list")

    def clear(self):
        self.__values = []

    def index(self, idx):
        try:
            return self.__values.index(idx)
        except ValueError:
            raise ValueError("Element is not in the list")

    def count(self, value):
        return self.__values.count(value)

    def reverse(self):
        return self.__values[::-1]

    def copy(self):
        return deepcopy(self.__values)