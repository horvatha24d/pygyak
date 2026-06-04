while True:
    szam1=int(input("Kérek egy egyjegyű pozitív számot (0-9): "))
    if 0 <= szam1 <= 9:
        break
   

print("Az ellenőrzött bekérés sikeres!")    

if szam1 % 2 == 0:
    print(f"A bekért szám ({szam1}) páros.")
else:
    print(f"A bekért szám ({szam1}) páratlan.")
