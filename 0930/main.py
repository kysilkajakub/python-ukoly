#**************************
# Kalkulačka spropitného
#30. 9. 2026
#**************************

print("KALKULAČKA SPROPITNÉHO")    # tisk nadpisu
celkova_cena = float(input("Zadej celkovou cenu: "))    # zadání celkové ceny
spropitne= int(input("Zadej spropitné: v %"))    
pocet_lidi = int(input("Zadej počet lidí: "))    
print(celkova_cena / pocet_lidi)    

celkova_cena_spropitne = celkova_cena + (celkova_cena * spropitne / 100)    # výpočet celkové ceny se spropitným
celkova_cena += celkova_cena * spropitne / 100 
print(celkova_cena)
cena_jeden =round( celkova_cena_spropitne / pocet_lidi +0.5)
print(f"Cena pro jednoho: {cena_jeden}")
