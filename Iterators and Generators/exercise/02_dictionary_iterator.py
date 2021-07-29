class dictionary_iter:
    def __init__(self, dict):
        self.dict = dict
        self.length = len(dict)
        self.keys = list(self.dict.keys())
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.length:
            key = self.keys[self.current]
            self.current += 1
            return key, self.dict[key]
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
