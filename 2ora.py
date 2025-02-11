szöveg = "A fekete cica átsétált az úton, hogy megegye az ott található párizsit."
print(szöveg)
print("A szöveg hossza:", len(szöveg))

szöveg_szavanként = szöveg.split(" ") # Feldarabolja a szöveget a szóközek mentén
print(szöveg_szavanként)

szöveg_azként = szöveg.split("az")
print(szöveg_azként)

első_n = szöveg.find("n")
print("Az 'n' karatker első előfordálásnak helye:", első_n)

első_az = szöveg.find("az")
print("Az 'az' karatkersorozat első előfordálásnak helye:", első_az)

print(szöveg.startswith("A"))
print(szöveg.startswith("x"))
print(szöveg.endswith("."))
print(szöveg.endswith("k"))

szó = "kUtYa"
print(szó)
print(szó.capitalize()) # Kutya
print(szó.lower())      # kutya
print(szó.upper())      # KUTYA

print("a cica története".title()) # Minden szót nagybetűvel kezd

print(szöveg.lower().count("a"))

# alt gr + Q -> \
# \n - enter
thing_1 = input("Type an object:\n")                # tárgy1
thing_2 = input("Type another object:\n")           # tárgy2
adjective = input("Give me an adjective:\n")        # tulajdonság
song_name = input("Give me the name of a song:\n")  # zene
celebrity = input("Give me a celebrity name:\n")    # híresség
feeling = input("Give me a feeling:\n")             # érzés
verb = input("Give me a verb:\n")                   # ige
place = input("Give me a place:\n")                 # hely
food = input("Give me a food item:\n")              # kaja
person = input("Give me a person/name:\n")          # ember

print(f"""
I just got back from a pizza party with {1}. 
Can you believe we got to eat {1} pizza in {1}?! 
Everyone got to choose their own toppings. 
I made '{1} and {1}' pizza, which is my favorite! 
They even stuffed the crust with {1}. How {1}! 
If that wasn't good enough already, {1} was there singing {1}. 
I was so inspired by the music, I had to get up out of my seat and {1}.
""")