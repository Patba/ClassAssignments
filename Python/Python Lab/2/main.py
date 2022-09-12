# nazwa_classic = ['samolot','marchewka','mecz','miecz','mieczyk','piorun','macierz','matka','atak',
#          'zenit','antena']
#
#
#
# def bubble_classic(a):
#     for _ in range(len(a)):
#         for i in range(1, len(a)):
#             if a[i]<a[i-1]:
#                 temp = a[i]
#                 a[i] = a[i-1]
#                 a[i-1] = temp
#
# bubble_classic(nazwa_classic)
# print(nazwa_classic)
#
#
# nazwa_modern = ['samolot','marchewka','mecz','miecz','mieczyk','piorun','macierz','matka','atak',
#          'zenit','antena']
#
# def bubble_modern(a):
#     for _ in range(len(a)):
#         for i in range(1, len(a)):
#             if a[i]<a[i-1]:
#                 a[i-1], a[i] = a[i], a[i-1]
#
# bubble_modern(nazwa_modern)
#
# print(nazwa_modern)


import os

f = open("dane.txt","r")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

f = open("dane.txt","r")
for x in f:
    print(x)
f.close()

f = open("dane.txt","r")
print(f.read())
f.close()


f = open("message.txt", "a", encoding="utf-8")
print(f.write("Wiadomosc \n"))
f.close()

f= open("message.txt", "r", encoding="utf-8")
print(f.read())
f.close()


if os.path.exists("message.txt"):
    os.remove("message.txt")
    print("Plik zostal usuniety")
else:
    print("plik nie istnieje")