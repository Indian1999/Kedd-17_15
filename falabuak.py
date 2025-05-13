print("1. feladat")
fordulok_szama = int(input("Add meg a fordulók számát: "))
print()

print("2. feladat")
golkulonbsegek = []
for i in range(1, fordulok_szama + 1):
    gk = int(input(f"{i}. fordulóban a gólkülönbség: "))
    golkulonbsegek.append(gk)
print()

print("3. feladat")
wins = 0
losses = 0
draws = 0
for item in golkulonbsegek:
    if item < 0:
        losses += 1
    elif item > 0:
        wins += 1
    else:
        draws += 1
print(f"A szezonban a csapatnak {wins} győzelme, {losses} veresége, {draws} döntetlene volt.")
print()

print("4. feladat")
pontok = wins * 3 + draws
print(f"A csapatnak a szezonban összesen {pontok} pontja lett.")
print()

print("5. feladat")
if wins > losses + draws:
    print("A csapatnak több győztes mérkőzése volt, mint veresége és döntetlene együttvéve.")
else:
    print("A csapatnak nem volt több győztes mérkőzése, mint veresége és döntetlene együttvéve.")
print()

print("6. feladat")
# Keressük meg az első győztes mérkőzést:
elso_win_index = 0
elso_win_gk = 0
for i in range(len(golkulonbsegek)):
    if golkulonbsegek[i] > 0:
        elso_win_index = i
        elso_win_gk = golkulonbsegek[i]
        break # kilép a ciklusból
utolso_win_gk = elso_win_gk
számláló = 0
for i in range(elso_win_index + 1, len(golkulonbsegek)):
    if golkulonbsegek[i] > utolso_win_gk:
        számláló += 1
    if golkulonbsegek[i] > 0:
        utolso_win_gk = golkulonbsegek[i]
print(f"A kitűzött célt {számláló} alkalommal sikerült elérnie a csapatnak.")