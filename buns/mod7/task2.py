def memoize(func):
    cache = {}

    def wrapped_func(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapped_func


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
