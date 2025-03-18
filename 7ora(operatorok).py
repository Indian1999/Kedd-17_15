# Operátorok (Műveleti jelek)
# +, -, *, /, //, %, =, >, ==, stb.

# Aritmetikai operátorok (matematikai művelet)

print(3 + 5)   # 8
print(9 - 2)   # 7
print(5 * 8)   # 40
print(40 / 8)  # 5.0 
# Mivel az osztás művelet nem zárt az egész számok halmazára (Nem tudjuk garantálni,
# hogy egész számot fogunk kapni), ezért az eredményt floatként tároljuk el
# akkor is ha amúgy egész számot kapunk eredményül
print(42 / 8) # 5.25
# Maradék nélküli osztás: Ez mindig egész értéket ad
print(42 // 8) # 5
print(40 // 8) # 5

# Maradékos osztás: (%) megadja az osztási maradékot
print(10 % 7) # 3, ez is mindig egész számot fog adni

# Hatványozás (**)
print(2**32) # 4294967296 2^32
print(10**3) # 1000

# Gyökvonást a hatványozással tudjuk megvalósítani
# négyzetgyök 16 = 16^(1/2)
# 6. gyök 16 = 16^(1/6)
print(25**(1/2)) # 5.0 (float)

# Aritmetikai operátorok összefoglalva:
# +   összeadás
# -   kivonás
# *   szorzás
# /   sima osztás (float-ot ad)
# //  maradék nélküli osztás (int)
# %   maradékos osztás
# **  hatványozás, ha gyököt vonni akarunk, akkor tört hatványra emelünk

# Értékadó operátorok (SZINTE bármi amiben =-jel van)
# egy változónak értéket ad
num = 10 # A num változónak a 10 értéket adja
print(f"num = {num}") # 10
num += 5 # A num értékéhez hozzáad 5-öt
print(f"num = {num}") # 15
num -= 3
print(f"num = {num}") # 12
num *= 4 
print(f"num = {num}") # 48
num /= 2
print(f"num = {num}") # 24.0 INNENTŐL KEZDVE A num egy float lesz
num //= 2
print(f"num = {num}") # 12.0
num **= 2
print(f"num = {num}") # 144.0
num %= 10
print(f"num = {num}") # 4.0

# Értékadó operátor (=, aritmetikai + =)

# Összehasonlító operátorok (True vagy False értéket ad)
# két értéket összehasonlít

print(5 > 1)  # True
print(5 < 2)  # False
print(5 == 8) # False
print(5 >= 5) # True
print(4 <= 2) # False
print(5 != 2) # True


# Logikai operátorok
# Logikai értékekkel kezdenek valamit
# (ÉS, VAGY, NEM) [and, or, not]
# Mindig egy logikai értéket ad eredményül
print(5 > 1 and 3 > 4) # True and False -> False
print(5 > 1 or 3 > 4)  # True or False  -> True
print(not 5 > 1)       # not True -> False

# Logikai kapuk:
# A | B | A és B | A vagy B | nem A | nem B
# i | i |    i   |    i     |   h   |   h
# i | h |    h   |    i     |   h   |   i
# h | i |    h   |    i     |   i   |   h
# h | h |    h   |    h     |   i   |   i

# Az in operátor
# Meghatározza, hogy x elem benne van-e egy adatszerkezetben
# 5 in lista
# True vagy False értéked
lista = [6,2,5,8,3]
print(5 in lista) # True
print(9 in lista) # False

szöveg = "kiscica"
print("c" in szöveg) # True
print("p" in szöveg) # False

# Bit szintű operátorok (ezekről majd később)
# &, |, ^, ~, <<, >>


# 1. feladat: Adott 2 lista
# Egyesítsük egy új listába ezt a kettőt úgy, hogy ne legyenek duplikációk
# Pálda kimenet: [43, 12, 75, 23, 99, 13, 54, 92, 11] (sorrend mindegy)
lista_1 = [43, 12, 75, 23, 99]
lista_2 = [13, 54, 43, 12, 92, 12, 11]
lista_3 = lista_1[:]
for item in lista_2:
    if item not in lista_3:
        lista_3.append(item)
print(lista_3)

# 2. feladat: Jelenítsünk meg egy a, b oldalú téglalapot
a = 5
b = 10
for i in range(a):
    print("#" * b)
print()
for i in range(a):
    if i == 0 or i == a-1:
        print("#" * b)
    else:
        print("#" + " "*(b-2) + "#")

# 3. feladat: Szöveg kódolás
# kimenet = "Kdlifgmetasöeeóon oo z  zvgt"
bemenet = "Kódolni fogom ezt a szöveget"

# 4. feladat: Olvassunk be egy számot és írjuk ki a szorzó tábláját
# Kimenet:
# 1 * 3 = 3
# 2 * 3 = 6
# 3 * 3 = 9
# ...
# 10 * 3 = 30
num = int(input("Adj meg egy 1-10 közötti egész számot!\n"))






