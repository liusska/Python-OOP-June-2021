def multiply(times):

    def decorator(function):
        def wrapper(num):
            result = 0
            for i in range(times):
                result += function(num)
            return result
        return wrapper
    return decorator

@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))


