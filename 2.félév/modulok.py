from random import randint, randrange, seed
from functools import cache
import math
import numpy as np # terminálba: pip install numpy
import matplotlib.pyplot as plt # python -m pip install matplotlib
from matplotlib.colors import LinearSegmentedColormap


def modul_bevezeto():
    seed(123)
    print(randint(5, 25))
    print(randint(5, 25))

    print(math.pi)
    print(math.tau)
    print(math.e)
    print(math.sqrt(2))
    print(math.inf > 97837498761398571349)
    print(math.nan)

    print(math.sin(60))
    print(math.ceil(4.00002))
    print(math.floor(4.00002))

    radius = 5
    print(f"A {radius} egység sugarú kör területe: {round(radius**2 * math.pi, 4)}")
    print(f"A {radius} egység sugarú kör területe: {round(radius**2 * 3.14, 4)}")

def numpy_modul():
    tomb = np.array([1,2,3,4,5])
    print(tomb)
    print(type(tomb))
    linear = np.linspace(-5, 4.9, 100)
    print(linear)
    print(linear.shape)
    linear = linear.reshape(5,5,4)
    print(linear)
    print(linear.shape)
    linear = linear.reshape(20, -1)
    print(linear)
    print(linear.shape)
    
mtx = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,1,1,0,0,1,1,0],
    [0,1,1,0,0,1,1,0],
    [0,0,0,1,1,0,0,0],
    [0,0,1,1,1,1,0,0],
    [0,0,1,1,1,1,0,0],
    [0,0,1,0,0,1,0,0]
]

my_cmap = LinearSegmentedColormap.from_list("creeper", ["green", "black"])
plt.imshow(mtx, cmap=my_cmap)
plt.axis("off")
plt.show()