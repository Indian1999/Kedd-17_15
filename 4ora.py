# Írjuk ki az első 10 természetes számot
i = 1
while i <= 10:
    print(i, end = " ")
    i += 1
print()

lista = []
bemenet = "default"
while bemenet != "":
    bemenet = input("Add meg a lista következő elemét!")
    if bemenet != "":
        lista.append(bemenet)

print(lista)