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

# Írjunk egy függvényt ami összeolvaszt két számot és visszaadja az eredményt
# (123, 456) -> 123456
# 123 + 456 = 579
# "123" + "456" = "123456"
def merge_numbers(num1, num2):
    return int(str(num1) + str(num2))

print(merge_numbers(123, 456))
print(merge_numbers(1, 324))

# Írjunk egy függvényt ami kap egy egész számot (n), illetve egy valamilyen másik értéket (value)
# és visszaad egy n elemből álló listát aminek mindden értéke value
# generate_list(3, "cica")   -> ["cica", "cica", "cica"]

def generate_list(n, value):
    lista = []
    for i in range(n):
        lista.append(value)
    return lista

print(generate_list(3, "asd"))
print(generate_list(5, True))
print(generate_list(8, 9))
print(generate_list(0, "asd"))
print(generate_list(4, ["asd", True, "9", 3.14]))


# Írjunk egy függvényt ami megkap egy listát, és visszaadja a listában található legnagyobb értéket!

def legnagyobb(lista):
    maximum = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > maximum:
            maximum = lista[i]
    return maximum

print(legnagyobb([1,2,3,52,32,324,23,23,432,324]))

# Írjunk egy függvényt ami megkap egy nevet és kiírja, hogy "Hello <név>!" (nem ad vissza semmit)

def say_hi(name):
    print(f"Hello {name}!")

say_hi("Sanyi")

# Írjunk egy függvényt ami megkap egy egész számot és egy logikai értéket, 
# ha logikai igaz, akkor visszaadja a szám tízszeresét,
# ha hamis, akkor visszaadja a szám felét

def func(num, logic):
    if logic:
        return num * 10
    else:
        return num // 2
    
print(func(8, True))
print(func(9, False))

