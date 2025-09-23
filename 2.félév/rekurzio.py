# A rekurzív függvény egy olyan függvény ami, önmagát hívja meg

# Faktoriális:
# 4! = 4 * 3 * 2 * 1 = 24
# 4! = 4 * 6 = 24
# 3! = 3 * 2 = 6
# 2! = 2 * 1 = 2
# 1! = 1
# 0! = 1
# n! = n * (n-1)!
# fakt(n) = n * fakt(n-1)

def fakt(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * fakt(n-1)

print(len(str(fakt(990))))

# Írjunkk egy függvényt az "a" rekurzív sorozat n. elemének kiszámítására
# a(n) = 5 + a(n-1)
# a(1) = -5
# a(3) = 5 + a(2) = 5 + 5 + a(1) = 5 + 5 + (-5) = 5

def a(n:int) -> int:
    if n <= 1:
        return -5
    return 5 + a(n-1)

print(a(8))

# b(n) = b(n-1) + b(n-2)
# b(1) = b(2) = 1

def b(n:int) -> int:
    if n == 1 or n == 2:
        return 1
    return b(n-1) + b(n-2)

for i in range(1, 15):
    print(b(i), end=" ")
print()


# c(n) = 3 * c(n-1) + 7      c(1) = -2
def c(n:int) ->int:
    if n == 1:
        return -2
    return 3 * c(n-1) + 7

print([c(i) for i in range(1, 14)])

# d(n) = d(n-1)**2 - 9 * d(n-2) - 10     # d(1) = 0,    d(2) = 3

def d(n:int) -> int:
    if n == 1:
        return 0
    if n == 2:
        return 3
    return d(n-1)**2 - 9 * d(n-2) -10

print([d(i) for i in range(1, 8)])

# e(n) = 2**(e(n-1))      e(1) = 0

def e(n:int) -> int:
    if n == 1:
        return 0
    return 2**e(n-1)
print([e(i) for i in range(1, 7)])



from functools import cache

@cache
def fib(n:int) -> int:
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

i = 1
while True:
    if i > 200:
        break
    print(f"fib({i}) = {len(str(fib(i)))}")
    i += 1



# Írjunk egy rekurzív függvényt, ami meghatározza egy lista elemeinek az összegét
# sum([]) = 0
# sum([n]) = n
# sum([n, m]) = n + sum([m])

def rek_sum(lista: list[int]) -> int:
    if len(lista) == 0:
        return 0
    if len(lista) == 1:
        return lista[0]
    return lista[0] + rek_sum(lista[1:])

print(rek_sum([6,34,342,67,54,34,34,34,34,54,67,67,67,2]))

# Hatványfüggvény rekurzívan
# a^b = a * a^(b-1)
# 2^3 = 2 * 2^2 = 2 * 2 * 2^1
def power(a:int, b:int) -> int:
    if a == 0 and b == 0:
        return "ERROR"
    if b == 0:
        return 1
    if b == 1:
        return a
    return a * power(a, b-1)

print(power(2, 10))