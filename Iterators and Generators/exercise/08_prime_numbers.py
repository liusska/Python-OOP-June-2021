def get_primes(data):
    for el in data:
        if el < 2:
            continue
        is_prime = True
        for num in range(2, el):
            if el % num == 0:
                is_prime = False
        if is_prime:
            yield el


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))