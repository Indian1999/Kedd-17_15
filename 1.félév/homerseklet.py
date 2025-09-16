legalacsonyabb = [-2, 0, -4, 3, 5, 2, 0, -3, 2, 4, 4, 2, 5, 7, 10]
legmagasabb    = [8, 10, 4, 6, 9, 10, 10, 5, 8, 15, 12, 6, 8, 15, 18]

# 1. feladat: Számítsuk ki minden napra, az adott napi hőingást (legnagyobb - legkisebb)
# az eredményt tároljuk el
hőingások = []
for i in range(len(legalacsonyabb)):
    hőingások.append(legmagasabb[i] - legalacsonyabb[i])
    
print(hőingások)

# 2. feladat: Írjuk ki, hogy hanyadik napon volt a legnagyobb hőingás
maxi = 0
for i in range(len(hőingások)):
    if hőingások[i] > hőingások[maxi]:
        maxi = i
print(f"A legnagyobb hőingás a {maxi + 1}. napon volt ({hőingások[maxi]} °C)")

# 3. feladat: Átlagosan mennyi volt egy nap a legmagasabb hőmérséklet
összeg = 0
for item in legmagasabb:
    összeg += item
print(f"Az átlagos napi legmagasabb hőmérseklet {round(összeg/len(legmagasabb), 1)} °C volt.")

# 4. feladat: Hány olyan nap volt ahol fagypont alá csökkent a hőmérséklet?
számláló = 0
for item in legalacsonyabb:
    if item < 0:
        számláló += 1
print(f"{számláló} napon csökkent a hőmérséklet fagypont alá")

# 5. feladat: Volt-e olyan nap ahol a napi hőingás nem volt nagyobb, mint 5 fok?
kisebb_mint_5 = False
for item in hőingások:
    if item <= 5:
        kisebb_mint_5 = True
        break

if kisebb_mint_5:
    print("Volt olyan nap amikor a napi hőingás nem volt nagyobb mint 5 °C.")
else:
    print("Nem volt olyan nap amikor a napi hőingás nem volt nagyobb mint 5 °C.")

# 6. feladat*: Hány olyan nap volt, amikor melegebb volt mint az előző nap 
# (a legalacsonyabb és legmagasabb hőmérséklet is nagyobb volt)
számláló = 0
for i in range(1, len(legalacsonyabb)):
    if legalacsonyabb[i-1] < legalacsonyabb[i] and legmagasabb[i-1] < legmagasabb[i]:
        számláló += 1
print(f"{számláló} napon fordult elő az, hogy melegebb volt, mint az előző nap")


# 7. feladat: Számoljunk minden napra átlag hőmérsékletet (legnagyobb/legkisebb számtani közepe)
átlagok = []
for i in range(len(legalacsonyabb)):
    átlagok.append((legalacsonyabb[i] + legmagasabb[i]) / 2)
print(átlagok)

# 8. feladat*: átlagosan hogyan változott napról napra a hőmérséklet 
összeg = 0
for i in range(1, len(legmagasabb)):
    összeg += átlagok[i] - átlagok[i-1]

átlag = összeg / (len(legmagasabb) - 1)

print(f"A hőmérséklet naponta átlagosan {round(átlag, 1)} °C-kal változott.")    
 