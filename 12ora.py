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

#2. feladat: határozzuk meg egy szám számjegyeinek az összegét

#3. feladat: Olvassuk be egy tört számlálóját és nevezőjét, majd hozzuk a lehető legegyszerűbb alakra a törtet pl.: 100/12 -> 25/3

#4. feladat: Legyen adott 2 tört, szorozzuk össze őket, és írjuk ki az eredményt a legegyszerűbb alakban

#5. feladat: Döntsük el egy számról, hogy tökéletes-e!
# Egy szám akkor tökéletes, ha az osztóinak összege (önmagát kivéve), pont az adott szám
# pl.: 6 = 1 + 2 + 3 = 6

#6. feladat: Adott egy lista
# Határozzuk meg a lista elemeinek átlagát
# Medián (középső elem) [3, 6, 7, 9, 13, 15, 17, 18, 20] 13
# [3, 6, 7, 9, 13, 14, 15, 17, 18, 20] -> (13 + 14) / 2 -> 13,5
# Szórás - A listában egy elem átlagosan, mennyivel tér el az átlagtól
# [1, 1, 2, 4, 5, 5] átlag: 3  szórás: (2+2+1+1+2+2) / 6 -> 5/3 = 1.66