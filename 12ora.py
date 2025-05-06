import random
import math
#1. feladat: Számoljuk meg hogy egy stringben hány mássalhangzó szerepel
szöveg = "A kiscica felmászott a fára, de sajnos nem tudott lejönni onnan."

mássalhangzók = "qwrtzpsdfghjklmnbvcxyQWRTZPLKJHGFDSYXCVBNM"
magánhangzók = "íaeuioőéáúűóüöÍAEUIOŐÚŰÓÜÖÁÉ"

vowel_counter = 0
constenant_counter = 0
space_counter = 0
special_counter = 0
for char in szöveg:
    if char in mássalhangzók:
        constenant_counter += 1
    elif char in magánhangzók:
        vowel_counter += 1
    elif char == " ":
        space_counter += 1
    else:
        special_counter += 1

print(szöveg)
print(f"Ebben a szövegben {vowel_counter} magánhangzó, {constenant_counter} mássalhangzó, {space_counter} szóköz és {special_counter} speciális karakter található.")
print(f"A szöveg {len(szöveg)} karakter hosszú.")

#2. feladat: 18:10 határozzuk meg egy szám számjegyeinek az összegét 18:10
def digit_sum(num):
    összeg = 0
    for char in str(num):
        if char != ".":
            összeg += int(char)
    return összeg

print(digit_sum(12345))
print(digit_sum(10000))
print(digit_sum(13.543))

#3. feladat: 18:15 Olvassuk be egy tört számlálóját és nevezőjét, majd hozzuk a lehető legegyszerűbb alakra a törtet pl.: 100/12 -> 25/3
def lnko(a, b):
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    oszto = 1
    for i in range(2, min(a,b) + 1):
        if a % i == 0 and b % i == 0:
            oszto = i
    return oszto

def simplify_fraction(számláló, nevező):
    oszto = lnko(számláló, nevező)
    return [számláló//oszto, nevező//oszto]

print(simplify_fraction(8, 4))
print(simplify_fraction(-80, 20))
print(simplify_fraction(100, 12))
print(simplify_fraction(1024, 64))

#4. feladat: 18:30 Legyen adott 2 tört, szorozzuk össze őket, és írjuk ki az eredményt a legegyszerűbb alakban
def multiply_fractions(frac1, frac2): # frac1 = [5, 3]
    szorzat = [frac1[0] * frac2[0], frac1[1] * frac2[1]]   
    return simplify_fraction(szorzat[0], szorzat[1]) 

print(multiply_fractions([3,5], [2,3]))
print(multiply_fractions([30,14], [2,39]))
print(multiply_fractions([-54,86], [54,12]))

#5. feladat: 18:40 Döntsük el egy számról, hogy tökéletes-e!
# Egy szám akkor tökéletes, ha az osztóinak összege (önmagát kivéve), pont az adott szám
# pl.: 6 = 1 + 2 + 3 = 6
# pl.: 1 + 2 + 4 + 7 + 14 = 28
def is_perfect(num):
    összeg = 0
    for i in range(1, num):
        if num % i == 0:
            összeg += i
    return összeg == num

tökéletesek = [i for i in range(1, 1001) if is_perfect(i)]
print(tökéletesek)

#6. feladat: 18:55 Adott egy lista
# Határozzuk meg a lista elemeinek átlagát
# Medián (középső elem) [3, 6, 7, 9, 13, 15, 17, 18, 20] 13
# [3, 6, 7, 9, 13, 14, 15, 17, 18, 20] -> (13 + 14) / 2 -> 13,5
# Szórás - A listában egy elem átlagosan, mennyivel tér el az átlagtól
# [1, 1, 2, 4, 5, 5] átlag: 3  szórás: (2+2+1+1+2+2) / 6 -> 5/3 = 1.66

def average(lista):
    összeg = 0
    for item in lista:
        összeg += item
    return összeg / len(lista)

def median(lista):
    sorted_lista = sorted(lista)
    if len(lista) % 2 == 0:
        return (sorted_lista[len(lista) // 2] + sorted_lista[len(lista) // 2 - 1]) / 2
    else:
        return sorted_lista[len(lista) // 2]

def deviation(lista):
    átlag = average(lista)
    összeg = 0
    for item in lista:
        összeg += math.fabs(átlag - item)
    return összeg / len(lista)

lista = [random.randint(-20, 200) for i in range(30)]
print(lista)
print("Átlag:",round(average(lista), 2))
print("Medián:",round(median(lista), 2))
print("Szórás:",round(deviation(lista), 2))