import random
import tkinter
import tkinter.messagebox 

def generate_puzzle():
    puzzle = ""
    while len(puzzle) != 4:
        digit = random.randint(0, 9)
        if str(digit) not in puzzle:
            puzzle += str(digit)
    return puzzle

def check_tipp():
    tipp = "1234"
    if len(tipp) != 4 or not tipp.isdigit() or len(set(tipp)) != 4:
        tkinter.messagebox.showwarning("Hiba", "4 különböző számjegyet adj meg!")
        return
    jo_szamok = 0
    jo_szamok_jo_helyen = 0
    for i in range(len(tipp)):
        if tipp[i] == puzzle[i]:
            jo_szamok_jo_helyen += 1
        elif tipp[i] in puzzle:
            jo_szamok += 1
    tippek += 1
    if jo_szamok_jo_helyen == 4:
        pass
    else:
        pass
    

puzzle = generate_puzzle() # pl.: 6843
tippek = 0
