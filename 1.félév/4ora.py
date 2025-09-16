# Írjuk ki az első 10 természetes számot
i = 1
while i <= 10:
    print(i, end = " ")
    i += 1
print()
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
összeg = 0
for item in lista:
    if item > 0:
        összeg += item
print("A lista pozitív elemeinek az összege:", összeg)
# 3. feladat: Melyik a legnagyobb szám?
max_index = 0
for i in range(len(lista)):
    if lista[i] > lista[max_index]:
        max_index = i
print("A legnagyobb szám:", lista[max_index])
# 4. feladat: Melyik a legkisebb szám?
min_index = 0
for i in range(len(lista)):
    if lista[i] < lista[min_index]:
        min_index = i
print("A legkisebb szám:", lista[min_index])
# 5. fealdat: Hány darab 10-nél nagyobb szám van a listában?
számláló = 0
for item in lista:
    if item > 10:
        számláló += 1
print(számláló, "db 10-nél nagyobb szám van a listában")
# 6. feladat: Határozzuk meg a lista elemeinek az átlagát!
print("A lista elemeinek az átlaga:", round(összeg/len(lista), 2))
# 7. feladat: Válogassuk szét a lista elemeit két másik listára: pozitívak és negatívak
pos_lista = []
neg_lista = []
for item in lista:
    if item < 0:
        neg_lista.append(item)
    if item > 0:
        pos_lista.append(item)
print("Pozitív számok:", pos_lista)
print("Negatív számok:", neg_lista)

for i in range(1, 11):
    for j in range(i):
        print(j+1, end = " ")
    print()
    
num = int(input("Adj meg egy egész számot!\n"))
prime = True
for i in range(2, num):
    if num % i == 0:
        prime = False
if prime:
    print("Ez egy prímszám.")
else:
    print("Ez egy összetett szám.")

