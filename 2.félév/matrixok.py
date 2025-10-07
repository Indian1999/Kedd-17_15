import random
import math
import numpy as np
import matplotlib.pyplot as plt

# Mátrix - lista ami listákat tárol
mtx = [
    [4, 3, 1, 6, 4, 7, 3],
    [0, 3, 1, 6, 1, 3, 2],
    [7, 3, 0, 6, 4, 0, 3],
    [1, 2, 0, 3, 7, 1, 2],
    [9, 8, 1, 9, 4, 0, 3]
]

print(mtx)
for row in mtx:
    print(row)
print(mtx[2][5]) # 0

# Programozási tételek mátrixokra:
# sor-oszlop vagy oszlop-sor bejárást alkalmazunk

# Összegzés tétele:
összeg = 0
for i in range(len(mtx)): # sorok száma
    for j in range(len(mtx[i])):
        összeg += mtx[i][j]
print(összeg)