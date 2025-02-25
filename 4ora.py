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