import os

PATH_FORRAS = os.path.join(os.path.dirname(__file__), "forras")

#a = input("Add meg az osztandót: ")
#b = input("Add meg az osztót: ")
a = 1
b = 2
#print(f"{a} / {b} = {a/b}") # TypeError: unsupported operand type(s) for /: 'str' and 'str'

# Ha nem számot adok meg: ValueError: could not convert string to float: '9ű'

# Ha a b-nek 0-t adok meg: ZeroDivisionError: float division by zero
try:
    print(f"{a} / {b} = {float(a) / float(b)}")
except TypeError:
    print("Típus hiba")
except ValueError:
    print("Mindenképpen számot adj meg!")
except ZeroDivisionError:
    print("0-val nem szabad osztani!")
except Exception:
    print("Ismeretlen hiba.")
finally:
    print("Osztás program vége.")

path = os.path.join(PATH_FORRAS, "story.txt")
try:
    with open(path) as f:
        print(f.read(50))
except FileNotFoundError:
    print("Nincs ilyen fájl:", path)
except PermissionError:
    print("You do not have permission to open this file:", path)
except Exception as ex:
    print("HIBA!")
    print(ex)



# RecursionError (soha nem érjük el a nullát)

def fakt(n):
    if type(n) != int:
        raise TypeError("The factorial function only takes positive integers!")
    if n < 0:
        raise ValueError("The factorial function only takes positive integers!")
    if n == 0:
        return 1
    return n * fakt(n-1)

num = 1321
try:
    print(fakt(num))
except TypeError as ex:
    print("Típus hiba!")
    print(ex)
except ValueError as ex:
    print("Érték hiba!")
    print(ex)
except Exception as ex:
    print("HIBA!")
    print(ex)


# Feladat: Írj egy függvényt ami megkap egy évszámot, és kiszámolja, hogy hány év telt el azóta.
# Ha nem integert adunk meg, dobjunk típus hibát
# ha a megadott évszám nagyobb mint 2026 (vagy az aktuális évszám bónusz feladatnak), akkor dobjunk Value Errort

def elapsed_years(year):
    if type(year) != int:
        raise TypeError("Az évszám egész érték kell, hogy legyen!")
    if year > 2026 or year < 0:
        raise ValueError("0 és 2026 közötti évszámot kell megadni!")
    return 2026 - year

# A függvény használatára írjunk egy programot, ami bekér a felhasználótól egy évszámot.
# És kiírja a függvény eredményét. MINDEN lehetséges hibát kezelj le!

year = "1999"#input("Add meg a születési éved: ")
try:
    print(elapsed_years(int(year)), "éves vagy.")
except TypeError as ex:
    print("Típus hiba!")
    print(ex)
except ValueError as ex:
    print("Érték hiba!")
    print(ex)
except Exception as ex:
    print("HIBA!")
    print(ex)


def average(lista):
    if type(lista) != list and type(lista) != tuple and type(set) != list:
        raise TypeError("Can only calculate the average of iterable objects.")
    if len(lista) == 0:
        raise ValueError("Cannot calculate the average of an empty list.")
    total = 0
    for item in lista:
        if type(item) != int and type(item) != float:
            raise TypeError("All list elements have to be numbers.")
        total += item
    return total / len(lista)

print(average([1,2,3,4,5]))
print(average(17.8))

