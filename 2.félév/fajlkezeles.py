import os
import random

path_olimpia = os.path.dirname(__file__) # Az a mappa, amiben a jelenleg futó script van
print(path_olimpia)
path_olimpia = os.path.join(path_olimpia, "olimpia.txt")
print(path_olimpia)

f = open("2.félév/olimpia.txt", "r", encoding="utf-8")
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