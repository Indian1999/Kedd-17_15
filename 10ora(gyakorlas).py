import random

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