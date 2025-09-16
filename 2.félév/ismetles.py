import random
print("Szia!")

név = "asd"#input("Hogy hívnak?\n")

print(f"Szia {név}!")

a = 432
b = 293

print(f"{a} + {b} = {a + b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} - {b} = {a - b}")

lista = [random.randint(-10, 10) for i in range(20)]
print(lista)

# Hány negatív szám van a listában?
számláló = 0
for item in lista:
    if item < 0:
        számláló += 1
print(f"{számláló} negatív szám van a listában.")

# Írjuk ki a számok átlagát!
összeg = 0
for item in lista:
    összeg += item
print(f"A listában található számok átlaga: { round(összeg/len(lista), 2) }")

# Mennyi a páros számok összege?
paros_osszeg = 0
for item in lista:
    if item % 2 == 0:
        paros_osszeg += item
print(f"A páros számok összege: {paros_osszeg}")

# Írjuk át a negatív számokat a listában a -10-szeresükre (-5 -> 50, -1 -> 10 stb....)
for i in range(len(lista)): # i = 0, 1, 2, ..., 19
    if lista[i] < 0:
        lista[i] = lista[i] * -10
print(lista)
