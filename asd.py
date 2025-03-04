import random

i = 0
while i < 10:
    print(i, end= " ")
    i += 2
print()

num = 694923321231
num_counter = 0
while num != 0:
    num //= 10
    num_counter += 1 

print ("total number of digits :", num_counter )
n = 10
print (f"Fibbonaci sorozat {n} eleme")
a = 1
b = 1
while n > 0:
    print(a,end = " ")
    c = a + b
    a = b
    b = c
    n -= 1
print()

num = random.randint(1, 100)
guesscount = 0
guesses = 0

while guesscount < 7 and guesses != num:
    guesses = int(input("tippelj egy számot"))
    if num > guesses:
        print ("ettől nagyobb")
    elif num < guesses:
        print ("ettől kisebb")
    guesscount += 1

if guesses == num:
    print("gg")
else : 
    print(f"sadge,{num} az a szám amire gondoltam")

stars_in_row = 1
starts = 7

while starts > 0:
    if stars_in_row == 1:
        print("*")
    if stars_in_row == 2:
        print("**")
    if stars_in_row == 3:
        print("***")
    if stars_in_row == 4:
        print("****")
    if stars_in_row == 5:
        print("*****")
    if stars_in_row == 6:
        print("*******")
    if stars_in_row == 7:
        print("********")
stars_in_row += 1
starts -= 1