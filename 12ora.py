#1. feladat: Számoljuk meg hogy egy stringben hány mássalhangzó szerepel
szöveg = "A kiscica felmászott a fára, de sajnos nem tudott lejönni onnan."

mássalhangzók = "qwrtzpsdfghjklmnbvcxyQWRTZPLKJHGFDSYXCVBNM"
magánhangzók = "íaeuioőéáúűóüöÍAEUIOŐÚŰÓÜÖÁÉ"

vowel_counter = 0
constenant_counter = 0
space_counter = 0
special_counter = 0
for char in szöveg:
    if char in mássalhangzók:
        constenant_counter += 1
    elif char in magánhangzók:
        vowel_counter += 1
    elif char == " ":
        space_counter += 1
    else:
        special_counter += 1

print(szöveg)
print(f"Ebben a szövegben {vowel_counter} magánhangzó, {constenant_counter} mássalhangzó, {space_counter} szóköz és {special_counter} speciális karakter található.")
print(f"A szöveg {len(szöveg)} karakter hosszú.")