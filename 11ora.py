# 1. feladat: Olvassuk be valaki születési dátumát (yyyy-mm-dd) és ez alapján 
# határozzuk meg, hogy hány napos az illető

birth_date = input("Add meg a születési dátumod (yyyy-mm-dd)")
birth_date = birth_date.split("-")
birth_date[0] = int(birth_date[0])
birth_date[1] = int(birth_date[1])
birth_date[2] = int(birth_date[2])

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

today = [2025, 4, 15]
months = ["buffer", 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = 0
while str(birth_date) != str(today):
    if birth_date[1] == 2 and birth_date[2] == 28 and is_leap_year(birth_date[0]):
        birth_date[2] += 1
    elif birth_date[1] == 2 and birth_date[2] == 29:
        birth_date[1] = 3
        birth_date[2] = 1
    elif birth_date[2] != months[birth_date[1]]:
        birth_date[2] += 1
    else:
        if birth_date[1] == 12:
            birth_date[0] += 1
            birth_date[1] = 1
            birth_date[2] = 1
        else:
            birth_date[1] += 1
            birth_date[2] = 1
    print(birth_date)
    days += 1
    
print("Ennyi napos vagy:", days)

# 2. feladat: Döntsük el két stringről, hogy anagrammák-e
# Pontosan ugan azokat a karaktereket tartalmazzák (és ugyan annyit belőlük)

# 3. feladat: Hány autónak kell lassítania?
# Ha egy auto előtt van egy másik autó aki lasabban megy, akkor lassítania kell
cars = [43, 76, 32, 54, 77, 91, 23, 45, 78, 99, 62, 48, 90, 99, 102]