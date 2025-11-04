# Számrendszerek
binary = bin(90)
print(binary) # 0b1011010   (0b jelezi, hogy ez egy bináris)
print(type(binary)) #<class 'str'>
print("0b nélkül:", binary[2:])

hexa = hex(4219)
print(hexa) # 0x107b     (0x jelzi, hogy 16-os számrendszer)
print(type(hexa)) #<class 'str'>
print(hexa[2:])

# Hol használjuk a 16-os számrendszert?
# RGB kódok színeknél   #FF1010    vörös szín (255 piros, 16 zöld, 16 kék)
# MAC címeknél   (A8-13-E6-2B-60-02)
# IPv6-os ip címek (fe80::2387:c34d:9be7:aeb7%17)^
# Memória címzésnél
class Valami:
    pass

var = Valami()
print(var) # <__main__.Valami object at 0x000001F79559F650>

octa = oct(90)
print(octa)   #0o132   (0o jelzi, hogy 8-as számrendszer)

# Egyéb számrendszerekből 10-esbe váltás

binary = "10110101011"
num = int(binary) # Alapesetben az int() fgv. 10-es számrendszerű számként értelmezi
print(num)
num = int(binary, 2)
print(num) # 1451

hexa = "3CF2"
num = int(hexa, 16)
print(num) #15602

# Mi van ha 16-ból akarunk 2-be?
binary = bin(int(hexa, 16))
print(binary) # 0b11110011110010

# Bináris operátorok

num1 = 42  
num2 = 97

print(num1 & num2) # 32
print(num1 | num2) # 107
print(num1 ^ num2) # 75            # alt gr + 3 (kétszer)

# Jobbra/Balra shiftelés

num = 42

print(num >> 1) # 21
print(num >> 2) # 10
print(num >> 3) #  5

print(num << 1) # 84
print(num << 2) #168
print(num << 3) #336

# Feladat: Határozzuk meg, hogy x GigaByte az TeraByte, MegaByte, KiloByte, Byte, bit
# 1 TB = 1024 GB
# 1 GB = 1024 MB
# 1 MB = 1024 KB
# 1 KB = 1024 B
# 1  B = 8 bit
# 1 bit = 1 db 1-es vagy 0-s

giga = int(input("Add meg a GigaByte-ok számát: "))
print(f"{giga} GB = {giga>>10} TB")
print(f"{giga} GB = {giga<<10} MB")
print(f"{giga} GB = {giga<<20} KB")
print(f"{giga} GB = {giga<<30} B")
print(f"{giga} GB = {giga<<33} bit")

# IP címek
ip = (192, 168, 1, 45)
mask = (255, 255, 255, 224)
print(f"Az ip címed: {ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}")
print(f"Hálózati maszk: {mask[0]}.{mask[1]}.{mask[2]}.{mask[3]}")

# Ha az ip címünket össze ÉS-eljük a hálózati maszkkal,
# megkapjuk a hálózat ip címét
print(f"A hálózat ip címe: {ip[0] & mask[0]}.{ip[1] & mask[1]}.{ip[2] & mask[2]}.{ip[3] & mask[3]}")