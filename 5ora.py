#Elől tesztelős ciklusok (while)

i = 0
while i < 10:
    print(i, end= " ")
    i += 2
print()

# feladat: Számoljuk meg egy szám, számjegyeit

num = 6948272659834
print(num)
számjegy_számláló = 0
while num != 0:
    num //= 10
    számjegy_számláló += 1
    
print("Számjegyek száma:", számjegy_számláló)

# feladat: Írjuk ki az első n db fibonacci számot!
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

n = 20
print(f"Fibonacci sorozat első {n} eleme:")
a = 1
b = 1
while n > 0:
     print(a, end = " ")
     c = a + b
     a = b
     b = c
     n -= 1
print()    
    
