# A tuple szinte ugyan az, mint a lista, a fő különbség, hogy a tuple nem módosítható

myTuple = (5, 2, 6)
print("myTuple:", myTuple)
print("type(myTuple):", type(myTuple))
print("myTuple[1] =", myTuple[1])
print("myTuple[0:2] =", myTuple[0:2])

# NEM módosítható
#myTuple[1] = 8
#TypeError: 'tuple' object does not support item assignment

#"asd123"[2] = "g" #a string is ilyen
#TypeError: 'str' object does not support item assignment

#myTuple.append(3) # AttributeError: 'tuple' object has no attribute 'append'
#myTuple += 3    # TypeError: can only concatenate tuple (not "int") to tuple
myTuple += (3,)
print(myTuple) # (5, 2, 6, 3)


empty_tuple = ()
print(empty_tuple)       # ()
print(type(empty_tuple)) # <class 'tuple'>

one_element_tuple = (3)
print(one_element_tuple)        # 3
print(type(one_element_tuple))  # <class 'int'>

# A (3) kifejezést aritmetikai kifejezésként értelmezi -> 3 értékű intre fog kiértékelődni


one_element_tuple = (3,)
print(one_element_tuple)        # (3,)
print(type(one_element_tuple))  # <class 'tuple'>

# Az elemek típusait szabadon lehet keverni
myTuple = (45, True, "kiscica", 3.13, 14, False, [1,2,3], (9, 8))

print(myTuple)

# tuple comprehension
myTuple = tuple(i for i in range(1, 11))
print(myTuple) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


# Operátorok tuple-re:

tuple1 = (1,2,3)
tuple2 = (4,5,6)
tuple3 = (3,2,1)
tuple4 = (4,5,6)

# Egyenlőség vizgsálat
print(tuple1 == tuple2) # False
print(tuple1 == tuple3) # False
print(tuple4 == tuple2) # True

print(f"tuple1 * 3 = {tuple1 * 3}") #  (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(f"tuple1 + 3 = TypeERROR") 
print(f"tuple1 + tuple2 = {tuple1 + tuple2}") # (1, 2, 3, 4, 5, 6)

from LogiLib.funcs import minimum

print(minimum([5,7,4,42,6,7,65,54,2,1,12,3,34,1,2,2,312,123])) # (9, 1)

import random
myTuple = tuple(random.randint(1, 20) for i in range(20))
print(myTuple)

# 1. feladat: Szerepel-e a tuple-ben egy 7-es érték?

if 7 in myTuple:
    print("Van benne hetes")
else:
    print("Nincs benne 7-es")

# 2. feladat: Határozzuk meg egy tuple elemeinek az összegét
összeg = 0
for item in myTuple:
    összeg += item
print("Összeg:", összeg)

# 3. feladat: Töröljük a listából a nem tuple típusú objektumokat
lista = [4, (1,3,4), [1, 9, "asd"], "asd", (1,), (5, 9, 1, 2), True]
new_lista = []
for item in lista:
    if type(item) == tuple:
        new_lista.append(item)
lista = new_lista[:]
print(lista)

# 4. feladat: Határozzk meg a tuple-ök elemeinek az átlagát
myTuple = ((1, 2, 3), (40, 13), (91, -23, 10), (-1, 0, 40, -50, 33))

# 5. feladat: Fordítsuk meg egy tuple elemeit
myTuple = (1, 2, 3, 4, 5, 6)   # -> (6, 5, 4, 3, 2, 1)

# 6. feladat: Ugyan ennek a tuplenek vágjuk le az első és utolsó elemét,
# majd mentsük el egy új tuple-be

# 7. feladat: Határozzuk meg, hogy egy tuple-ben melyik indexen található az első kétjegyű szám

# 8. feladat:  Számoljuk ki a vector-műveletek eredményét
a = (3, 5)
b = (-1, 3)
c = (2, -1)
# Határozzuk meg az       a + 2b - 3c vektort



