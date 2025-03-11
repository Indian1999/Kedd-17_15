nevek = ["András", "Béla", "Cecil", "Dénes", "Elemér", "Ferenc"]
print(nevek)
print(type(nevek))
print("A lista elemszáma:", len(nevek))

print(nevek[0]) # András
print(nevek[3]) # Dénes
print(nevek[len(nevek) - 1]) # Ferenc
# Pythonban, megadhatunk negatív indexet
print(nevek[-1]) # Hátulról az első elem (Ferenc)
print(nevek[-4]) # Hátulról a 4. elem (Cecil)

# Intervallumos indexelésre is van lehetőségünk

print(nevek[2:5]) 
# 2. indextől az 5. indexig adja vissza elemeket
# kezdet zárt, a vég nyitott intervallum (a 2. indexü már benne van, de
# az 5. indexü elem már nem lessz benne)
# ["Cecil", "Dénes", "Elemér"]

print(nevek[:4])
# Ha a : elé nem írunk semmit, akkor a lista elejétől fogja nézni
# a 4 ugyanúgy nyílt intervallumon van, tehát nem lesz benne
# ["András", "Béla", "Cecil", "Dénes"]

print(nevek[2:])
# Ha a : mögé nem írok semmit, akkor a lista végéig fog menni
# Így az utolsó elem is benne lesz
# ["Cecil", "Dénes", "Elemér", "Ferenc"]

print(nevek[:]) # Az összes

nevek2 = nevek
print(nevek2)
# Amikor egy listát egy másik listával teszünk egyenlővé, akkor valójában nem fog másolat készülni,
# hanem csak annyi történik, hogy létrehozunk egy új "pointert" (elnevezést) ugyan annak a listának
# Ugyan arra a listára 2 változó hivatkozik (A memóriában csak 1szer van eltárolva)

nevek2[2] = "Csaba"
print(nevek2)
print(nevek)

# Amiatt, mert a nevek2 és a nevek lista, ugyan arra a listára mutatnak, ezért ha az egyiken módosítunk
# akkor a másik módosul

# Hogyan lehet ezt megoldani?

# 1. lehetőség:

nevek2 = nevek[:] # Ez így már a memóriában létre fog hozni egy új listát
nevek2[2] = "Cica"
print(nevek2)
print(nevek)

# 2. lehetőség:

nevek2 = nevek.copy()
nevek2[2] = "Cirmos"
print(nevek2)
print(nevek)


#Lista elemeinek a megfordítása:

nevek = nevek[::-1]
print(nevek) #['Ferenc', 'Elemér', 'Dénes', 'Csaba', 'Béla', 'András']

# Milyen lehetőségeink vannak egy lista bejárására?

# Klasszik: while (elől tesztelős) ciklus

i = 0
while i < len(nevek):
    print(nevek[i], end= " ")
    i += 1
print()

# Számlálós ciklus (for)

for i in range(len(nevek)):
    print(nevek[i], end= " ")
print()

# foreach ciklus (for)

for item in nevek: # item = "Ferenc", "Elemér", "Dénes", ...
    print(item, end = " ")
print()

# Vegyítve a két for ciklust

for index, item in enumerate(nevek):
    print(f"{index}: {item}", end= " ")
print()

# range() függvény:

for i in range(len(nevek)): # 0 1 2 3 4 5 
    print(i, end = " ")
print()

for i in range(5, 10): # 5 6 7 8 9 és a 10 már nincs benne
    print(i, end = " ")
print()

for i in range(10, 100, 20): # 10 30 50 70 90 
    print(i, end = " ")
print()

for i in range(len(nevek) - 1, -1, -1): # 5 4 3 2 1 0
    print(i, end = " ")
print()

""" How to crash a computer
for i in range(100000):
    f = open(f"trash/trash{i}.txt", "w")
    f.write(str(type(nevek))*10000)
    f.close()
"""

# Generáljunk listákat:

lista = []
for i in range(10):
    lista.append(i)
print(lista)

# 1. feladat: