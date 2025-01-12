import random

pot1 = "ang_besede.txt"
pot2 = "slo_besede.txt"
tocke = 0
ponovi = 0
ponovi_besede = []
print("Angleška igra: ")
print("Pravila igre: ")
print("Ta igra te testira koliko angleških besed poznaš.\nTi moraš samo povedati pravilno besedo.")

with open(pot1, 'r', encoding='utf-8') as file:
    ang_besede = [line.strip() for line in file]
with open(pot2, 'r', encoding='utf-8') as file:
    slo_besede = [line.strip() for line in file]

for i in range (1, 11):
    izbrano = random.randint(0, 9)
    beseda_rac = ang_besede[izbrano]
    beseda = input("Vnesi slovensko besedo za besedo " + str(beseda_rac) + ": ")
    if beseda == slo_besede[izbrano]:
        tocke += 1
        print("Napisal si pravilno besedo. Točke: "+str(tocke)+"/"+str(i))
    else:
        ponovi += 1
        ponovi_besede.append(beseda_rac)
        print("Beseda se ne ujema. Točke: "+str(tocke)+"/"+str(i))
print("Tukaj so besede, ki jih nisi vedel: ")
print(", ".join(ponovi_besede))
print("-------------------------------------------------------------------")
print("Dosežene točke:", tocke)
print("Dosežen odstotek: "+str(int((tocke/10)*100))+"%")