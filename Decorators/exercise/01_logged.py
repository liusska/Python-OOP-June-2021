def logged(function):
    def wrapper(*args):
        result = f"you called {function.__name__}{args}"
        result += "\n" + f"it returned {function(*args)}"
        return result

    return wrapper


@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))
