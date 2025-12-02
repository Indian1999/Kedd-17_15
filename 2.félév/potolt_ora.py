import random
"""
list = []
for i in range(5):
    list.append(input("írj valamit"))
for j in list:
    print(j)
"""
"""
a = input("első")
b = input("második")
c = input("harmadik")

print(a,b,c,sep=",")

types = input("konvertálás típusa kg,c,m")
x = float(input("Érték"))
eredmeny = 0
if types == "kg":
    unit = input("Mértékegység")
    if unit  == "kg":
        print(str(x) + "g in kg"+str(x*1000))
    elif unit == "g":
        print(str(x) + "kg in g"+str(x/1000))
    else:
        print("dumb")
elif types == "c":
    unit = input("Mértékegység")
    if unit  == "c":
        print(str(x) + "c in f"+str((x*1.8)+32))
    elif unit == "f":
        print(str(x) + "f in c"+str((x-32)/1.8))
    else:
        print("dumb")
elif types == "km":
    unit = input("Mértékegység")
    if unit  == "km":
        print(str(x) + "m in km"+str(x*1000))
    elif unit == "m":
        print(str(x) + "km in m"+str(x/1000))
    else:
        print("dumb")
else:
    print("ilyet nem tudok konvertálni")
print(f"az érték {eredmeny}")

time = input("Kezdés ideje: (xx;xx)")
duration = int(input("ideje?????????? (percben pls)"))
hour,min = time.split(";")
time_minutes = int(hour)*60+int(min)
end_minutes = time_minutes+duration
end_hour = end_minutes//60
end_min = end_minutes - (end_minutes//60)*60
print("Vége: "+str(end_hour)+":"+str(end_min))


num = int(input())
collatz = [num]
while num !=1:
    if num % 2 == 0:
        num = num/2
        collatz.append(int(num))
    else:
        num = 3*num+1
        collatz.append(int(num))
print(collatz)
"""


# 6.feladat
numbers = [x for x in range(1,36)]
for item in range (len(numbers)):
    if numbers[item] % 3 == 0 and "3" in str(numbers[item]):
        numbers[item] = "bimbum"
    elif numbers[item] % 3 == 0:
        numbers[item] = "bim"
    elif "3" in str(numbers[item]):
        numbers[item] = "bum"
print(numbers)

password = input()
characters = ["&","@","#","$"]
if len(password) >= 6 and len(password) <= 16:
    print("jó hosszúság")
else:
    print("nem jó hosszuság")
for i in password:
    if i.islower():
        print("van benne kisbetű")
    elif i.isupper():
        print("van benne nagybetű")
    elif i in characters:
        print("tiltott karakter van")
    elif i.isdigit():
        print("van benne szám")


list = []
a = int(input("A oldal:"))
b = int(input("B oldal:"))
c = int(input("C oldal:"))
list.append(a,b,c)

if (a+b > c) and (a+c > b) and (c+b > a):
    print("megrajolhazó")
else: 
    print("nem megrajzolható")

if (a==b) and (b==c):
    print("egyenlő oldalú")
elif (a==b) or (b==c) or (c==a):
    print("egyenlő szárú")
else:
    print("sima")

maximum = min(list)
minimum = max(list)
list.remove(minimum)
list.remove(maximum)
middle = list[0]

if minimum**2 + middle**2 == maximum**2:
    print("derékszögű")


names = ["John","Nicka","Paul"]
goals = [5,5,2]
fault = [2,9,5]

print(f"legtöbb gol:{names[goals.index(max(goals))]}")
print(f"legkevesebb:{names[goals.index(min(goals))]}")

avarage = []
for i in range(len(goals)):
    avarage.append(goals[i]-fault[i])

print(f"legjobb gamer:{names[avarage.index(max(avarage))]}")

variable = True
for i in range(len(goals)):
    if goals[i] >3:
        if fault[i] >= 5:
            variable = False

print(f"volt-e gamer(3+ gól,5- hiba): {variable}")

print(f"gól szám:{str(sum(goals))}")
print(f"hiba szám:{str(sum(fault))}")
print(f"átlag gólok:{str(sum(goals)/len(goals))}")

count = 0
top_scorers = ""
for i in range(len(goals)):
    if goals[i] > 3:
        count += 1
        top_scorers += str(names[i]) + ", "

print(f"összeszen {count} top scorer volt és ezek {top_scorers}")

count_a = 0
for i in names:
    num = i.count("a")
    count_a += num
print(f"összese {count_a} db 'a' volt a gyerekek nevében")
