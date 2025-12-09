import os
import random

path_olimpia = os.path.dirname(__file__) # Az a mappa, amiben a jelenleg futó script van
print(path_olimpia)
path_olimpia = os.path.join(path_olimpia, "forras", "olimpia.txt")
print(path_olimpia)

f = open(path_olimpia, "r", encoding="utf-8")
#szöveg = f.read()

#for line in f:
#    print(line.strip())

lines = f.readlines()
#print(lines)
f.close()

szöveg = ""
f = open(path_olimpia, "r", encoding="utf-8")

szöveg = f.read()

f.close()
print(szöveg)

# Fájlkezelésnél ajánlott a context manager használata

with open(path_olimpia, "r", encoding="utf-8") as f:
    print(f.read(50))

# with-en kívül, már nem lesz megnyitva a fájl

def generate_matrix(rows, cols):
    mtx = []
    for i in range(rows):
        lista = []
        for j in range(cols):
            lista.append(random.randint(0, 70))
        mtx.append(lista)
    return mtx

matrix = generate_matrix(38, 5)
output_path = os.path.dirname(__file__)
output_path = os.path.join(output_path, "matrix.txt")
with open(output_path, "w", encoding="utf-8") as f:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j != len(matrix[i]) -1:
                f.write(f"{matrix[i][j]};")
            else:
                f.write(f"{matrix[i][j]}")
        f.write("\n")


# Olvassuk be és tároljuk el a homerseklet.txt fájlban található adatokat
homersekletek = []
path_homerseklet = os.path.join(os.path.dirname(__file__), "forras", "homerseklet.txt")
with open(path_homerseklet, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip().split(";") # ['33', '31', '-1', '3', '3', '-7', '26']
        sor = [int(item) for item in line]
        homersekletek.append(sor)

# Hozzunk letre egy homerseklet_elemzes.txt fájlt aminek a tartalma:
# Az átlag hőmérséklet: x
# A leghidegebb hőmérséklet: x
# A leghidegebb nap az év x. napján volt
# A heti szintű átlaghőmérséklet: [3, 8, -2, 7, 3, 12, ....] (52 elem)

összeg = 0
day_counter = 0
for i in range(len(homersekletek)):
    for j in range(len(homersekletek[i])):
        összeg += homersekletek[i][j]
        day_counter += 1
atlag = összeg / day_counter

leghidegebb = (0, 0)
for i in range(len(homersekletek)):
    for j in range(len(homersekletek[i])):
        mini, minj = leghidegebb
        if homersekletek[i][j] < homersekletek[mini][minj]:
            leghidegebb = (i, j)
nap = leghidegebb[0]*7 + leghidegebb[1] + 1

heti_atlag = []
for i in range(len(homersekletek)):
    összeg = 0
    for j in range(len(homersekletek[i])):
        összeg += homersekletek[i][j]
    heti_atlag.append(round(összeg/len(homersekletek[i]),1))

path_homerseklet_elemzes = os.path.join(os.path.dirname(__file__), "homerseklet_elemzes.txt")
with open(path_homerseklet_elemzes, "w", encoding="utf-8") as f:
    f.write(f"Az éves átlag hőmérséklet: {round(atlag, 1)}\n")
    f.write(f"Az év leghidegebb napján {homersekletek[leghidegebb[0]][leghidegebb[1]]} °C volt.\n")
    f.write(f"Ez a nap az év {nap}. napja volt.\n")
    f.write(f"A heti szintű átlag hőmérsékletek: {heti_atlag}\n")