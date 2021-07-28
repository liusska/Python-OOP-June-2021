class reverse_iter:
    def __init__(self, args):
        self.args = args
        self.start = len(self.args) - 1
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration
        index = self.start
        self.start -= 1
        return self.args[index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
