from itertools import permutations


def possible_permutations(data):
    for per in permutations(data):
        yield list(per)


[print(n) for n in possible_permutations([1, 2, 3])]