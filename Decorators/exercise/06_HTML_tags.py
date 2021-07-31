def tags(param):
    def decorator(func):
        def wrapper(*args):
            return f"<{param}>{func(*args)}</{param}>"
        return wrapper
    return decorator


@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
