liczby = [56,89,100,23,45,68,90,29,91,101,77,88,34,58,66,82]

def pokaz_stat(lista):
    minimum = min(lista)
    maksimum = max(lista)
    return minimum, maksimum


wynik = pokaz_stat(liczby)

print(wynik)

mini,maxi = pokaz_stat(liczby)

print(mini)


def get_srednia_odchyl(lista):
   average = sum(lista)/len(lista)
   skalowanie = [x/average for x in lista]
   skalowanie.sort(reverse=True)
   return skalowanie

longest, *middle, shortest = get_srednia_odchyl(liczby)

print(longest)
