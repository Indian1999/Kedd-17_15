# 1. feladat: Olvassuk be, hogy hány versenyző eredményeit szeretnénk beolvasni
n = int(input("Add meg a versenyzők számát: "))

# 2. feladat: Olvassunk be ennyi eredményt, előösször a versenyző nevét, utána
# a versenyző elért pontszámát (0 - 100) egész szám
nevek = []
pontok = []
for i in range(1, n + 1):
    nevek.append(input(f"{i}. versenyző neve: "))
    pontok.append(int(input(f"{nevek[-1]} pontszáma: ")))

# 3. feladat: Határozzuk meg a versenyzők átlagos pontszámát
# (1 tizedes jegyre kerekítve)

összeg = 0
for item in pontok:
    összeg += item
print("A pontszámok átlaga:", round(összeg / n, 1))

# 4. feladat: Írjuk ki, hogy ki nyerte a versenyt és hogy hány pontot ért el
# (Ha több nyertes van, akkor mindet írjuk ki)
maxi = 0
for i in range(1, n):
    if pontok[i] > pontok[maxi]:
        maxi = i
nyertes_indexek = []
for i in range(n):
    if pontok[i] == pontok[maxi]:
        nyertes_indexek.append(i)
print("A legnagyobb pontszámot elért versenyző(k):")
for index in nyertes_indexek:
    print(f"{nevek[index]} - {pontok[index]} pont")        

# 5. feladat: Hány olyan versenyző volt aki kerek pontszámot ért el 
# (0, 5, 10, 15, ..., 95, 100)
számláló = 0
for item in pontok:
    if item % 5 == 0:
        számláló += 1
print(f"{számláló} versenyző ért el kerek pontszámot.")

# 6. feladat: Kérjünk be egy pontszámot a felhasználótól és írjuk ki,
# hogy kik azok, akik ezalatt teljesítettek
pontszam = int(input("Adj meg egy pontszámot és megkeresem, hogy kik azok akik ettől rosszabbúl teljesítettek: "))
for i in range(n):
    if pontok[i] < pontszam:
        print(f"{nevek[i]} - {pontok[i]} pont")