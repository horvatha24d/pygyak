import random

def jotermes(szam):
    return szam >= 5

gyumolcsfak = ["almafa", "szilvafa", "eperfa", "körtefa", "barackfa", "cseresznyefa"]
gyumolcsfak.append("diófa")

osszesen = 0
jo_fak = 0

for fa in gyumolcsfak:
    termes = random.randint(1, 10)
    print(f"{fa} - {termes} db termés")
    osszesen += termes
    if jotermes(termes):
        jo_fak += 1

atlag = osszesen // len(gyumolcsfak)

print(f"Összesen {osszesen} db termés volt a kertben.")
print(f"Átlagosan {atlag} db termés volt a fákon.")
print(f"A kertben {jo_fak} db fa volt, ami elegendő (jó) termést hozott.")  