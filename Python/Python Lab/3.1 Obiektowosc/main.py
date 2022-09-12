class Osoba:

    kolor_oczu = "niebieski"

    #opis stanu
    def __init__(self, imie, wiek, waga, wzrost):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.info()



    def info(self):
        print("Tworzenie nowej instancji klasy osoba")

    def print_osoba(self):
        print(f'osoba - imie: {self.imie}, wiek: {self.wiek} lat, waga: {self.waga} kg, wzrost: {self.wzrost} cm')

    def wiekza10lat(self):
        return self.wiek + 10

    def czypracownik(self):
        return False
    def bmi(self):
        return self.waga/(self.wzrost/100)**2
    def opis_bmi(self):
        if self.bmi() < 18.5:
            return "niedowaga"
        elif self.bmi() <= 25:
            return "waga prawdilowa"
        elif self.bmi() <= 30:
            return "nadwaga"
        else:
            return "otylosc"

    def policz_ppm(self, plec):
        if plec == "K":
            return 655.1 + 9.563 * self.waga + 1.85 * self.wzrost - 4.676 * self.wiek
        elif plec == "M":
            return 66.5 + 13.75 * self.waga + 5.003 * self.wzrost - 6.775 * self.wiek
        else:
            return "nie ma takiej płci...."

p1 = Osoba("Jan", 25, 60, 180)

print(f'Kolor oczu: {p1.kolor_oczu}')

p1.print_osoba()

print(f"bmi ciala wynosi: {p1.bmi()}, opis: {p1.opis_bmi()}.1f")



print(f'Wiek za 10 lat: {p1.wiekza10lat()}')

p2 = Osoba("Piotr", 43, 82, 190)

p2.kolor_oczu = "piwne"

print(f'p2 kolor oczu: {p2.kolor_oczu}')
print(f'wiek za 10 lat: {p2.wiekza10lat()}')
p2.print_osoba()


class Pracownik(Osoba):

    #konstruktor z dziedziczeniem
    def __init__(self, imie, wiek, waga, wzrost, firma, stanowisko, placa, lata_pracy):
        super().__init__(imie, wiek, waga, wzrost)
        self.firma = firma
        self.stanowisko = stanowisko
        self.placa = placa
        self.lata_pracy = lata_pracy

    def print_pracownik(self):
        print(f"dane pracownika - firma: {self.firma}, stanowisko: {self.stanowisko}, placa: {self.placa} zł, lata_pracy: {self.lata_pracy}")

    def czypracownik(self):
        return True


print("********************************************")

em1 = Pracownik("Karol", 41, 99, 172, "DN", "CEO", 12000, 10)

print(f"kolor oczu: {em1.kolor_oczu}")
em1.print_osoba()
em1.print_pracownik()
print(f"czy pracownik: {em1.czypracownik()}")


class Sport:

    def __init__(self, dyscyplina, lataupr, best_wynik):
        self.dyscyplina = dyscyplina
        self.lataupr = lataupr
        self.best_wynik = best_wynik

    def infosport(self):
        print(f"Dyscyplina: {self.dyscyplina}, lata uprawiania sportu: {self.lataupr},"
        f"życiówka: {self.best_wynik}")

class Ekstra:
    pass

class Student(Pracownik, Sport, Ekstra):
    #klasa wielodziedzicaca
    #konstruktor z wielodziedziczeniem
    def __init__(self, imie, wiek, waga, wzrost, nr_studenta, kierunek, rokukon, firma = "", stanowisko = "", placa = "", lata_pracy = "", dyscyplina = "", lataupr ="", best_wynik = ""):
        Pracownik.__init__(self, imie, wiek, waga, wzrost, firma, stanowisko, placa, lata_pracy)
        Sport.__init__(self, dyscyplina, lataupr, best_wynik)
        self.nr_studenta = nr_studenta
        self.kierunek = kierunek
        self.rokukon = rokukon

    def print_student(self):
        print(f"dane studenta: {self.nr_studenta}, kierunek: {self.kierunek}, rokukon: {self.rokukon}")

    def czypracownik(self):
        if self.firma == "":
            return False
        else:
            return True

print("*********************************************")

s2 = Student("Paula", 21, 58, 172, 756756, "informatyka", 2024, "ABX", "junior developer", 3500, 1)
s2.print_osoba()
s2.print_pracownik()
s2.print_student()
