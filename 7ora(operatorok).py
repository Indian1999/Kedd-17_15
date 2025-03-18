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