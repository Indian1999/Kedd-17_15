# 1. a, feladat: Váltsunk át x kilogrammot grammba
#kg = int(input("Add meg hogy hány kilogramm\n"))
kg = 6
print(f"{kg} kg = {kg*1000} g")
# 1. b, feladat: Váltsunk át x grammot kilogrammba
#g = int(input("Add meg hogy hány gramm\n"))
g = 5432
print(f"{g} g = {g/1000} kg")

# Fahrenheit = 1.8 * Celsius + 32
# Celsius = (Fahrenheit - 32) / 1.8 
# 2. a, feladat: Fahrenheitből Celsiusba
fahr = 90
print(f"{fahr} °F = {(fahr - 32) / 1.8} °C")
# 2. b, feladat: Celsiusból Fahrenheit-be
celsius = 43
print(f"{celsius} °C = {1.8 * celsius + 32} °F") 

# 1 km = 0.62137 mérföld
# 3. a, feladat: km-ből mérföldbe
km = 41
print(f"{km} km = {km*0.62137} mi")

# 3. b, feladat: mérföldből km-be
mi = 58
print(f"{mi} mi = {mi/0.62137} km")

# 4. feladat: Nézzük a számokat 1-től 75-ig
# Ha egy szám osztható 3-mal, akkor írjuk ki, hogy bim
# Ha egy számban szerepel a 3-mas számjegy írjuk ki, hogy bam
# Ha osztható 3-mal és szerepel hármas akkor: bimbam

for i in range(1, 76):
    if i % 3 == 0 and "3" in str(i):
        print(i, "bimbam")
    elif i % 3 == 0:
        print(i, "bim")
    elif "3" in str(i):
        print(i, "bam")

# 5. feladat: Ellenőrizzük, hogy egy jelszó elég erős-e
# A hossza 6 és 16 karakter között van
# Van benne kis és nagybetű is
# Van benne szám
# Van benne különleges karakter
special_chars = "&@.-,*-?%<>!^ˇ~"
password = "KetrecHarc!"
correct_length = len(password) >= 6 and len(password) <= 16
has_lower_case = False
has_upper_case = False
has_digit = False
has_special = False

for char in password:
    if char.isdigit():
        has_digit = True
    if char.islower():
        has_lower_case = True
    if char.isupper():
        has_upper_case = True
    if char in special_chars:
        has_special = True 
if correct_length and has_lower_case and has_upper_case and has_digit and has_special:
    print("Elég erős a jelszó")
else:
    print("A jelszó túl gyenge!")

# 6. feladat: Adottak egy háromszög 3 oldalának hossza
# Adjuk meg, hogy a háromszög, derék szögű, egyenlő szárú, szabályos, vagy egyik sem
# Ha nem létezik ilyen háromszög, írjuk ki hogy ilyen háromszög nem létezik
a = 3
b = 4
c = 5

if a + b > c and a + c > b and b + c > a:
    print("Létezik a háromszög!")
    print(a**2)
    print(b**2)
    print(c**2)
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Derékszögű")
    if a == b and b == c:
        print("Szabályos háromszög")
    elif a == b or b == c or a == c:
        print("Egyenlő szárú háromszög")
else:
    print("Nem létezik ilyen háromszög!")


# 7. feladat: Egy futóversenyen ezek az időeredmények születtek:
nevek = ["Józsi", "Gábor", "Ferenc", "István", "János", "Károly"]
eredmények = [43.2, 49.6, 52.2, 43.8, 41.9, 46.0]
# Írjuk ki, hogy ki nyerte a versenyt