class sequence_repeat:
    def __init__(self, data, count):
        self.data = data
        self.count = count
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.index
        while self.count > 0:
            self.index += 1
            self.count -= 1
            if self.index > len(self.data):
                self.index = 1
                temp = 0
            return self.data[temp]
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
