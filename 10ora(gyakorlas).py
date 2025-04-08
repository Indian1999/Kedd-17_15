import random
import math

# 1. feladat: Szedjük ki a duplikációkat a listából
szamok = [4, 1, 3, 9, 2, 8, 1, 8, 2, 4, 6, 3, 1, 0, 2, 5, 3, 2]

seen = []
for item in szamok:
    if item not in seen:
        seen.append(item)
print(seen)

# másik megoldás:
# set-ben minden elem csak egyszer szerepelhet
no_duplactions = list(set(szamok))
print(no_duplactions)

# extend() függvény
lista1 = [6,3,2,9,2,18,1]
lista2 = [8,4,2,0,2,6,8,8]
lista3 = [1,2,3,4,5,6]
#lista2 elemeit rakjuk bele lista1
for item in lista2:
    lista1.append(item)
print(lista1)

lista1.extend(lista3)
print(lista1)

# Válagassuk ki az int típusú objektumokat egy listából (egész számok)
lista = [4, 4.12, True, False, "cica", 5, 6.0, 8, [1,2,3], 9, 4.2321, 0]
integer_lista = []
for item in lista:
    if type(item) == int:
        integer_lista.append(item)
print(integer_lista)

# 2. feladat: Határozzuk meg egy lista legnagyobb és legkisebb elemének különbségét
lista = [random.randint(1, 1000) for i in range(10)]
print(lista)
minimum = lista[0]
maximum = lista[0]
for item in lista:
    if item > maximum:
        maximum = item
    if item < minimum:
        minimum = item

print("legnagyobb - legkisebb:", maximum - minimum)
# 3. feladat: Határozzuk meg a lista legnagyobb és 2. legnagyobb elemét

# Egyszerű cserés rendezés:
for i in range(len(lista) - 1):
    for j in range(i + 1, len(lista)):
        if lista[i] < lista[j]:
            lista[i], lista[j] = lista[j], lista[i]
print(lista)
print("Legnagyobb:", lista[0])
print("2. legnagyobb:", lista[1])


# 4. feladat: Határozzuk meg egy tetszőleges függvény Zérus Helyét

# Könnyebb feladat: csak egész szám lehet a ZH
# Nehezebb feladat: mivan ha nem csak egész szám lehet a ZH
# Mivan ha több zérushely van?


def linear(x):
    return 2 * x + 4

def absolute(x):
    return math.fabs(x - 2) - 10

def squared(x):
    return (x - 6) * (x + 2)

func = squared
y = func(0)
i = 1
while y != 0:
    y = func(i)
    if y == 0:
        break
    y = func(-i)
    if y == 0:
        i = -i
        break
    i += 1
print("Zérushely: x =", i)

