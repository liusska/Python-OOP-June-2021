def type_check(type_for_check):
    def decorator(func):
        def wrapper(data):
            if not isinstance(data, type_for_check):
                return "Bad Type"
            return func(data)
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))
