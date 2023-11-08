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


@validate_args
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
print(fibonacci())
print(fibonacci(5, 5))
print(fibonacci('5'))
print(fibonacci(-5))