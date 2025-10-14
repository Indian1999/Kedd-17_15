import random
from rekurzio import fib

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

# Feladat: Készítsünk egy felsoroló függvényt, ami két index közötti fibonacci számot határozza meg

def fib_generator(from_num, to_num):
    if from_num < 1:
        return "minimum 1 legyen a from_num"
    for num in range(from_num, to_num):
        yield fib(num)

for item in fib_generator(1, 8):
    print(item, end=" ")
print()

def yield_evens(lista):
    for item in lista:
        if item % 2 == 0:
            yield item

for item in yield_evens([5,86,4,6,67,6,7,34,34,67,56,56,34,53,2,4,7,5,56,76,76,5,2]):
    print(item, end=" ")
print()

lista = [i for i in fib_generator(8, 15)]
print(lista)

# Írjunk egy generátor függvényt ami az 
# a(n) = a(n-1) + 5 
# a(1) = 2
# sorozat elemeit sorolja fel
def a(n):
    value = 2
    for i in range(1, n+1):
        yield value
        value += 5

print([item for item in a(10)])

# Írjunk egy generátor függvényt, ami megkap egy stringet és felsorolja a stringben található összes magánhanzót
def yield_vowels(string):
    vowels = "óüöűúőoieáéaíÓÜÖŰÚŐOIEÁÉAÍ"
    for char in string:
        if char in vowels:
            yield char

print([char for char in yield_vowels("A kiscica felmászott a fára.")])

# Írjunk egy prímszámokat generáló függvényt, a függvény egy paramétert kap (n), az első n prímszámot kell legenerálnunk

def is_prime(num):
    for i in range(2, num//2 +1):
        if num % i == 0:
            return False
    return True

def prime_generator(n):
    counter = 0
    num = 2
    while True:
        if is_prime(num):
            yield num
            counter += 1
            if counter == n:
                break
        num += 1

print([i for i in prime_generator(20)])

# Készítsünk egy olyan generátor függvényt, ami egy bármilyen szűrőt alkalmaz egy listán
def is_even(num):
    return num % 2 == 0

def is_two_digit(num):
    return 10 <= num and 99 >= num

def filter_list(lista, func):
    for item in lista:
        if func(item):
            yield item
lista = [random.randint(1, 100) for i in range(20)]
evens = [i for i in filter_list(lista, is_even)]
two_digits = [i for i in filter_list(lista, is_two_digit)]
primes = [i for i in filter_list(lista, is_prime)]

print(lista)
print(evens)
print(two_digits)
print(primes)

