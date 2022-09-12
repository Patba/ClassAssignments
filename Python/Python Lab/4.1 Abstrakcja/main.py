class Square:

    def __init__(self, bok):
        self.bok = bok

    def policzpole(self):
        return self.bok ** 2


class Rectangle:

    def __new__(cls, szer: float, wys: float):
        if szer == wys:
            return Square(bok=szer)
        return object.__new__(Rectangle)

    def __init__(self, szer: float, wys: float):
        self.szer = szer
        self.wys = wys

    def policzpole(self):
        return self.szer * self.wys



r1 = Rectangle(12, 8)
r2 = Rectangle(6, 6)

print(type(r1))
print(type(r2))

print(f"pole prostokata: {r1.policzpole()}")
print(f"pole kwadratu: {r2.policzpole()}")