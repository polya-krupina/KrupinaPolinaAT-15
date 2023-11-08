import time


def timer(func):
    def wrapped_func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} was performed for {end - start} seconds")
        return result
    return wrapped_func


def memoize(func):
    cache = {}

    def wrapped_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapped_func


def validate_args(func):
    def wrapped_func(*args, **kwargs):
        if len(args) < 1:
            return "Not enough arguments"
        if len(args) > 1:
            return "Too many arguments"
        argument = args[0]
        if not isinstance(argument, int):
            return "Wrong types"
        if argument < 0:
            return "Negative argument"
        return func(*args, **kwargs)
    return wrapped_func


@timer
def test_func(func, n):
    return func(n)


@validate_args
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print('Without memoize:')
print(test_func(fibonacci, 30))
fibonacci = memoize(fibonacci)
print('\nWith memoize:')
print(test_func(fibonacci, 30))