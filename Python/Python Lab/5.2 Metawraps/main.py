from functools import wraps


def debug(func):
    @wraps
    def wrapper(*args, **kwargs):
        print(f"pełna nazwa metody: {func.__qualname__}")
        return func(*args, **kwargs)

    return wrapper()


def debugmethods(cls):
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug(val))

    return cls


class debugMeta(type):

    def __new__(cls, clsname, bases, clsdict):
        obj = super().__new__(cls, clsname, bases, clsdict)
        obj = debugmethods(obj)
        return obj


class Base(metaclass=debugMeta): pass


class Calc(Base):

    def add(self, x, y):
        return x + y


class Calc_m(Base):

    def mul(self, x, y):
        return x * y


obl1 = Calc()
obl2 = Calc()

x = 10
y = 20

print(obl1.add(x, y))
