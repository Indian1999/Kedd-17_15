import random

def generate_puzzle():
    puzzle = ""
    while len(puzzle) != 4:
        digit = random.randint(0, 9)
        if str(digit) not in puzzle:
            puzzle += str(digit)
    return puzzle

puzzle = generate_puzzle() # pl.: 6843

gameOn = True
tipp = ""
tippek = 0
while gameOn:
    tipp = input("Adj meg 4 számjegyet szóközek nélkül (pl.: 0123)\n")
    jo_szamok = 0
    jo_szamok_jo_helyen = 0
    for i in range(len(tipp)):
        if tipp[i] == puzzle[i]:
            jo_szamok_jo_helyen += 1
        elif tipp[i] in puzzle:
            jo_szamok += 1
    tippek += 1
    if jo_szamok_jo_helyen == 4:
        gameOn = False
    else:
        print("Jó számok jó helyen:", jo_szamok_jo_helyen)
        print("Jó számok, de nem jó helyen:", jo_szamok)
print(f"Szép volt! {tippek} lépéstből rájöttél, hogy a megoldás {puzzle} volt.")