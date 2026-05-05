# Határozzuk meg a páratlan számok összegét
lista = [34,4,21,45,54,76,56,43,3,45,54,56,67,67]

ptlan_összeg = 0
for item in lista:
    if item & 1: # 1-el való éseléskor a páratlanok 1-et adnak
        ptlan_összeg += item
print(ptlan_összeg)

# Írj egy programot ami kiszámolja, hogy x GB-nan hány, MB, KB, B van
# /, // használata nélkül
gb = 13
print(f"{gb} GB = {gb << 10} MB") # * 1024
print(f"{gb} GB = {gb << 20} KB")
print(f"{gb} GB = {gb << 30} B")
print(f"{gb} GB = {gb << 33} bit")

# List comprehension módszerrel, generáljuk le a kövi listákat:
# pl.: [i for i in range(5)]

# Páros számok, 10-től, 40-ig
lista = [i for i in range(10, 41, 2)]
print(lista)

# Az első 10 négyzetszám
lista = [i**2 for i in range(1, 11)]
print(lista)

# az első 50 eleme az (an) = 5*n-11   sorozatnak  
lista = [5*i -11 for i in range(1, 51)]
print(lista)
lista = [i for i in range(-6, -6 + 50*5, 5)]
print(lista)