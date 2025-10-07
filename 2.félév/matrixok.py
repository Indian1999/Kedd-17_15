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
    [3, 8, 1, 2, 4, 0, 3]
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

# Elndöntés tétele: (Van-e 9-es szám a mátrixban?)
van_kilenc = False
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        if mtx[i][j] == 9:
            van_kilenc = True
            break # kilép a ciklusból

print(van_kilenc)

# Maximum kiválasztás:
maximum = mtx[0][0]
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        if mtx[i][j] > maximum:
            maximum = mtx[i][j]
print("maximum:", maximum)

# Megszámlálás tétele: (számoljuk meg, hogy hány páratlan szám van a mátrixban)
szamlalo = 0
for i in range(len(mtx)):
    for j in range(len(mtx[i])):
        if mtx[i][j] % 2 == 1:
            szamlalo += 1
print("Páratlanok:", szamlalo, "db")


# List comprehension
lista = [i**2 for i in range(1, 11)]
print(lista) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

mtx = [[i,i**2, "szomszéd"] for i in range(7)]
print(mtx)

mtx = [[random.randint(0, 100) for j in range(10)] for i in range(8)]
for row in mtx:
    print(row)

mtx3d = [[[k for k in range(4)] for j in range(3)] for i in range(5)]
print(mtx3d)

összeg = 0
for i in range(len(mtx3d)):
    for j in range(len(mtx3d[i])):
        for k in range(len(mtx3d[i][j])):
            összeg += mtx3d[i][j][k]
print(összeg)


# Kockák ábrázolása matplotlibbel és numpy-al

axes = [5, 5, 5]
cube = np.ones(axes) # Létrehoz egy 5*5*5-ös mátrixot, tele egyesekkel
colors = np.empty(axes + [3]) # Létrehoz egy 5*5*5*3-as mátrixot, üres értékekkel
# axes + [3] - > [5,5,5,3]
colors[0] = [1, 0, 0] # Piros
colors[1] = [0, 1, 0] # Zöld
colors[2] = [0, 0, 1] # Kék
colors[3] = [0, 1, 1] # Türkiz
colors[4] = [1, 1, 0] # Sárga

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.voxels(cube, facecolors=colors, edgecolors="black", alpha=0.5)

plt.close()

tér = np.ones([8,8,8])
colors = np.empty([8,8,8,3])
colors[:] = [0,1,0]
colors[2][0][0] = [0,0,0]
colors[5][0][0] = [0,0,0]
colors[2][0][1] = [0,0,0]
colors[3][0][1] = [0,0,0]
colors[4][0][1] = [0,0,0]
colors[5][0][1] = [0,0,0]
colors[2][0][2] = [0,0,0]
colors[3][0][2] = [0,0,0]
colors[4][0][2] = [0,0,0]
colors[5][0][2] = [0,0,0]
colors[3][0][3] = [0,0,0]
colors[4][0][3] = [0,0,0]
colors[5][0][4:6] = [0,0,0]
colors[6][0][4:6] = [0,0,0]
colors[1][0][4:6] = [0,0,0]
colors[2][0][4:6] = [0,0,0]

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.voxels(tér, facecolors=colors)
plt.axis("off")
plt.close()


data = np.random.randint(0, 2, size = (8,8,8))
data = np.random.choice([0, 1], size = (8,8,8), p = [0.9, 0.1])
colors = np.random.random(size = (8,8,8,3))

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.voxels(data, facecolors=colors)
plt.axis("off")
plt.close()

data = np.zeros((32,32,32))
for i in range(400):
    probabilities = [1/100 for i in range(32)]
    probabilities[16] = 69/100
    x,y,z = np.random.choice([i for i in range(0, 32)], size = 3, p = probabilities)
    data[x][y][z] = 1


fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.voxels(data)
plt.axis("off")
plt.show()