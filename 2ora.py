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
