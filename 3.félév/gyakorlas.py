# 3. feladat:

mantissza = 3.5 #float(input("Mantissza (float): "))
kitevő = 2#int(input("Kitevő (int): "))

print(f"A szám tényleges értéke: {mantissza * 10**kitevő}")
print(f"Tudományos alak: {mantissza}e{kitevő}")

if mantissza > 0:
    print("A szám pozitív")
elif mantissza < 0:
    print("A szám negatív")
else:
    print("Nulla.")

# 5. feladat:
num = int(input("Adj meg egy potenciális prímet: "))
is_prime = True

if num % 2 != 0:
    for i in range(3, num//3 + 1, 2):
        if num % i == 0:
            print(i)
            is_prime = False
            break
elif num != 2:
    is_prime = False

if is_prime:
    print("Ez egy prím.")
else:
    print("Ez nem prím")

def factorisation(num):
    oszto = 2
    osztok = []
    while num != 1:
        while num % oszto != 0:
            oszto += 1
        osztok.append(oszto)
        num //= oszto
    return osztok

print(factorisation(4096))

#6. feladat:
n = 5 # int(input("n: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i*j, end = " ")
    print()

# 4. feladat:
"""
90-100: Jeles (5)
•75-89: Jó (4)
•60-74: Közepes (3)
•40-59: Elégséges (2)
•0-39: Elégtelen (1)"""
num = 67 #int(input("pontszám: "))
if num >= 90:
    print("Jeles (5)")
elif num >= 75:
    print("Jó (4)")
elif num >= 60:
    print("Közepes (3)")
elif num >= 40:
    print("Elégséges (2)")
else:
    print("Elégtelen (1)")

