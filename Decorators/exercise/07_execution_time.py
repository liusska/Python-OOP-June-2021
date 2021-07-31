from timeit import default_timer as timer


def exec_time(func):
    def wrapper(*args):
        start_time = timer()
        func(*args)
        end = timer() - start_time
        return end
    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 10000000))
