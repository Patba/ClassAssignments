import math
from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, a, b):
        self.a = a
        self.b = b


    @abstractmethod
    def policz_pole(self):
        pass




class Prostokat(Figura):
    def policz_pole(self):
        return self.a * self.b




class Trojkat(Figura):
    def policz_pole(self):
        return self.a * self.b/2




pr = Prostokat(5.5, 6.77)

print(pr.policz_pole())

tr = Trojkat(5, 7.1)

print(tr.policz_pole())


class Trapez(Figura):


    def __init__(self, a, b, h):
        super().__init__(a,b)
        self.h = h

    def policz_pole(self) -> float:
        return (self.a + self.b) * self.h/2


trp = Trapez(6.4, 5.2, 4.6)

print(trp.policz_pole())


#Stworz klase kolo dziedziaczac klase Figura policz jego pole dla promienia 5.5

class Kolo(Figura):

    def __init__(self, a):
        super().__init__(a, 0)

    def policz_pole(self) -> float:
        return math.pi * pow(self.r, 2)



kl = Kolo(19.25)
print(f"pole kola: {kl.policz_pole():.2f}")



