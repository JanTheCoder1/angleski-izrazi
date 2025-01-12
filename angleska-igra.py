import random

rdeca = '\033[31m'
reset = '\033[0m'
zelena = '\033[32m'
pot1 = "ang_besede.txt"
pot2 = "slo_besede.txt"
tocke = 0
ponovi = 0
izbrano = 0
ponovi_besede = []
ponovljeno = []
stevilo_angleskih_besed = 119
stevilo_sprasevanj = 10 # Ne more jih biti več kot stevilo_angleshih_besed
print("Angleška igra: ")
print("Pravila igre: ")
print("Ta igra te testira koliko angleških besed poznaš.\nTi moraš samo povedati pravilno besedo.")

with open(pot1, 'r', encoding='utf-8') as file:
    ang_besede = [line.strip() for line in file]
with open(pot2, 'r', encoding='utf-8') as file:
    slo_besede = [line.strip() for line in file]

for i in range (1, stevilo_sprasevanj+1):
    izbrano = random.randint(0, stevilo_angleskih_besed-1)
    while izbrano in ponovljeno:
        izbrano = random.randint(0, 9)
    ponovljeno.append(izbrano)
    beseda_rac = ang_besede[izbrano]
    beseda = input("Vnesi slovensko besedo za besedo " + zelena + str(beseda_rac) + reset + ": ")
    if beseda == slo_besede[izbrano]:
        tocke += 1
        print(zelena + "Napisal si pravilno besedo. " + reset + "Točke: "+str(tocke)+"/"+str(i))
    else:
        ponovi += 1
        ponovi_besede.append(beseda_rac)
        print(rdeca + "Beseda se ne ujema. Točke: " + reset +str(tocke)+"/"+str(i))
print("Tukaj so besede, ki jih nisi vedel: ")
print(rdeca + ", ".join(ponovi_besede) + reset)
print(zelena + "-------------------------------------------------------------------")
print("Dosežene točke:", tocke)
print("Dosežen odstotek: "+str(int((tocke/10)*100))+"%" + reset)