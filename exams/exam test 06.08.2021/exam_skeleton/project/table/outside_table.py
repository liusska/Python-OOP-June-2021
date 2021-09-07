from project.table.table import Table


class OutsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self._table_number

    @table_number.setter
    def table_number(self, value):
        if value < 51 or value > 100:
            raise ValueError("Outside table's number must be between 51 and 100 inclusive!")
        self._table_number = value


