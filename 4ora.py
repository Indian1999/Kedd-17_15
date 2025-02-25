# Írjuk ki az első 10 természetes számot
i = 1
while i <= 10:
    print(i, end = " ")
    i += 1
print()

lista = []
bemenet = "default"
while bemenet != "":
    #bemenet = input("Add meg a lista következő elemét!\n")
    bemenet = ""
    if bemenet != "":
        lista.append(bemenet)

print(lista)

for i in range(10): # i = 0, 1, 2, ..., 7, 8, 9
    print(i, end= " ")
print()

for i in range(5, 15): # i = 5, 6, 7, ... 12, 13, 14 (a 15 már nem)
    print(i, end= " ")
print()

for i in range(2, 100, 10): # i = 2, 12, 22, 32, ..., 82, 92
    print(i, end= " ")
print()
# range(5) = [0,1,2,3,4]
# range(5, 10) = [5,6,7,8,9]
# range(0, 10, 2) = [0,2,4,6,8]

for i in range(100, 10, -10): # i = 100, 90, 80, ..., 30, 20
    print(i, end= " ")
print()

lista = ["Anna", "Beáta", "Cecil", "Dénes", "Elemér", "Ferenc"]
for item in lista: # item = "Anna", "Beáta", ..., "Elemér", "Ferenc"
    print(item, end = " ")
print()

for i in range(len(lista)):
    print(lista[i], end = " ")
print()

lista = [11, -4, 7, 1, 6, -5, -12, 0, 11, 14, -8, -9, 2, 23, 11, 10, -4, 0, 18, 4, 8, 1, 1, 11]
print(lista)
# 1. feladat: Határozzuk meg a lista elemeinek az összegét!
összeg = 0
for item in lista:
    összeg += item
print("A lista elemeinek az összege:", összeg)
# 2. feladat: Határozzuk meg a pozitív számok összegét!

# 3. feladat: Melyik a legnagyobb szám?

# 4. feladat: Melyik a legkisebb szám?

# 5. fealdat: Hány darab 10-nél nagyobb szám van a listában?

# 6. feladat: Határozzuk meg a lista elemeinek az átlagát!

# 7. feladat: Válogassuk szét a lista elemeit két másik listára: pozitívak és negatívak