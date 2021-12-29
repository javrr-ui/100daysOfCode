def add(*args):
    return sum(args)


print(add(3, 5))


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]

    return n


print(calculate(3, add=5, multiply=4))
