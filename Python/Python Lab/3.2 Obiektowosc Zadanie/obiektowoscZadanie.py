class Pojazd:

    def __init__(self, cena, waga, ilosc_kol, marka, miejsca):
        self.cena = cena
        self.waga = waga
        self.ilosc_kol = ilosc_kol
        self.marka = marka
        self.miejsca = miejsca

    def info_pojazd(self):
        print(f'Pojazd o cenie: {self.cena} i wadze: {self.waga}, koła: {self.ilosc_kol}, marka: {self.marka}')


class Rower(Pojazd):

    def __init__(self, cena, waga, ilosc_kol, typ_roweru, miejsca):
        super().__init__(cena, waga, ilosc_kol, miejsca)
        self.typ_roweru = typ_roweru


    def info_rower(self):
        print(f"Rower typu {self.typ_roweru}, waga: {self.waga}, cena: {self.cena}")


class Tir(Pojazd):
    def __init__(self, cena, waga, ilosc_kol, marka, konie_mechaniczne, miejsca):
        super().__init__(cena, waga, ilosc_kol, marka, miejsca)
        self.konie_mechaniczne = konie_mechaniczne


    def info_tir(self):
        print(f"Rower marki {self.marka}, waga: {self.waga}, cena: {self.cena}, posiada {self.konie_mechaniczne} koni mechanicznych, koła: {self.ilosc_kol}")


class Terenowy(Pojazd):
    def __init__(self, cena, waga, ilosc_kol, marka, miejsca,konie_mechaniczne, dyferencjal, naped_na_cztery):
        super().__init__(cena, waga, ilosc_kol, marka, miejsca)
        self.konie_mechaniczne = konie_mechaniczne
        self.dyferencjal = dyferencjal
        self.naped_na_cztery = naped_na_cztery

    def info_terenowy(self):
        print(f"Pojazd terenowy marki {self.marka}, waga: {self.waga}, cena: {self.cena}, posiada {self.konie_mechaniczne} koni mechanicznych, koła: {self.ilosc_kol}, czy dyferencjal: {self.dyferencjal}, naped_na_cztery: {self.naped_na_cztery}")





dupa = Pojazd(1000000, 20, 3, "Dupsztal", 4)
dupa.info_pojazd()



