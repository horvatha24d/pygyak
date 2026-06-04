class Sutemeny:
    def __init__(self, nev: str, tipus: str, ar: int):
        self.nev = nev
        self.tipus = tipus
        self.ar = ar


sutik = []

f = open("cuki.txt", "r", encoding="utf-8")
for sor in f:
    sor = sor.strip()
    if sor != "":
        nev, tipus, ar = sor.split(";")
        sutik.append(Sutemeny(nev, tipus, int(ar)))
f.close()

print("d) feladat:")
print(f"A cuki.txt-ben összesen {len(sutik)} sütemény található.")

osszes_vegyes = 0
for suti in sutik:
    if suti.tipus == "vegyes":
        osszes_vegyes += suti.ar

print("e) feladat:")
print(f"A vegyes sütemények ára összesen {osszes_vegyes} Ft.")

f = open("akciosTortak.txt", "w", encoding="utf-8")
for suti in sutik:
    if "torta" in suti.nev.lower() and suti.ar < 10000:
        akcios_ar = round(suti.ar * 0.9)
        f.write(f"{suti.nev};{suti.tipus};{akcios_ar}\n")
f.close()

print("f) feladat: fájlbaírás")