data = ['F5.3', 'NF1', 'F3.2', 'NF0.6', 'NF0', 'F2.1', 'NF2']

print("2. feladat")
km = 0
for szakasz in data:
    if szakasz[0]  == "F":
        km += float(szakasz[1:])
    else:
        km += float(szakasz[2:])
print(f"A verseny távja {km} km volt.")
print()

print("3. feladat")
if data[-1][0] == "F":
    print("Futva ért célba.")
else:
    print("Gyalogolva ért célba.")
print()

print("4. feladat")
számláló = 0
for item in data:
    if item == "NF0":
        számláló += 1
print(f"A verseny során {számláló} alkalommal állt meg.")
print()

print("5. feladat")
f_számláló = 0
for item in data:
    if item[0] == "F":
        f_számláló += 1

if data[-1][0] == "F":
    print(f"A futást {f_számláló - 1} alkalommal szakította meg.")
else:
    print(f"A futást {f_számláló} alkalommal szakította meg.")
print()

print("6. feladat")
megallt = False
for i in range(len(data) - 1):
    if data[i][0] == "N" and data[i+1][0] == "N":
        megallt = True
        break
if megallt:
    print("Volt olyan alkalom, hogy gyaloglás után közvetlenül megállt.")
else:
    print("Nem volt olyan alkalom, hogy gyaloglás után közvetlenül megállt.")
    