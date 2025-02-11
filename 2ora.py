szöveg = "A fekete cica átsétált az úton, hogy megegye az ott található párizsit."
print(szöveg)
print("A szöveg hossza:", len(szöveg))

szöveg_szavanként = szöveg.split(" ") # Feldarabolja a szöveget a szóközek mentén
print(szöveg_szavanként)

szöveg_azként = szöveg.split("az")
print(szöveg_azként)
