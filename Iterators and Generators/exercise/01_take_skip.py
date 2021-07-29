class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current_step = 1
        self.value = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_step > self.count:
            raise StopIteration
        current_value = self.value
        self.value += self.step
        self.current_step += 1
        return current_value


numbers = take_skip(10, 5)
for number in numbers:
    print(number)

