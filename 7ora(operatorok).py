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