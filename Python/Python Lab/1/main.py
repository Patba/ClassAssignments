def przelicznik(swtch, m):
    if(swtch == 1):
        return m/1850
    elif(swtch == 2):
        return m/1609.344
    elif(swtch == 3):
        return m/0.9144
    elif(swtch == 4):
        return m/0.30477
    elif(swtch == 5):
        return m/0.0254

print("Wybierz opcje (1 - mila morska, 2 - mila ladowa, 3 - jard, 4 - stopa, 5 - cal: ")
a = int(input())

print("Wpisz ile masz metrów ;)")
b = int(input())

print(przelicznik(a,b))

#jak stworzyc kalkulator liczacy dowolne miary w dowolnym kierunku metrycznym (metr,cm,m...) <-> anglosaskie
