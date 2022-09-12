class Switch(object):
    value=None

    def __new__(cls, value):
        cls.value = value

        return True



def case(*args):
    return any((arg == Switch.value for arg in args))


n = int(input("Podaj Cyfre [0-9]: "))

while Switch(n):
    if case(0):
        print("cyfra 0")
        break
    if case(1, 4, 9):
        print("n jest kwadratem innej liczby")
        break
    if case(2):
        print("n jest liczba parzysta")
        break

    if case(2, 3, 5, 7):
        print("n jest liczba pierwsza")
        break