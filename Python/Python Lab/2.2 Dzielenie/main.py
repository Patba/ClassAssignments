# def dziel(x,y):
#     try:
#         wynik = x/y
#     except ZeroDivisionError:
#         print("Dzielenie przez zero")
#     except NameError:
#         print("Brak zmiennej")
#     except TypeError:
#         print("Nie dziel wartości tekstowych")
#     else:
#         print(f"Wynik dzielenia: {format(wynik)}")
#     finally:
#         print("Policzmy coś jeszcze")
#
#
# dziel(60,0)
# dziel(-20,-2)
# dziel(10,-2)
# dziel(100,2)
# dziel(10,150)
# dziel(10,1)

def silnia(n):
    if n<0:
        raise ValueError("silnia niezdefiniowana dla liczb ujemnych")
    wynik = 1
    for i in range(1,n+1):
        wynik *= i
    return wynik

def silnia_rek(n):
    if n<0:
        raise ValueError("silnia niezdefiniowana dla liczb ujemnych!")
    if n == 0:
        return 1
    else:
        return n*silnia_rek(n-1)


try:
    print("podaj argument silni n: ")
    n = int(input())
    print(f'silnia z n = {n} wynosi: {silnia(n)}')
except ValueError as e:
    print(e)