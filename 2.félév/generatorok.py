import random

def func(x):
    for i in range(10):
        if i == x:
            return # kilép a függvényből
    print("Függvény vége")

func(4)  # Nem történik semmi
func(46) # Függvény vége

# Felsoroló függvények: (yield)

def négyzet_számok():
    i = 1
    while True:
        yield i**2 # Visszaadja i négyzetét, de nem állítja le a függvényt
        i += 1

for num in négyzet_számok():
    print(num, end = " ")
    if num > 100:
        break
print()

def myRange(upperBound):
    i = 0
    while i < upperBound:
        yield i
        i += 1

for i in myRange(5):
    print(i, end=" ") # 0 1 2 3 4
print()

