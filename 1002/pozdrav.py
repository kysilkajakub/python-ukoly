cas= float(input("kolik je hodin?"))
if cas<0:
    print(f"-1čas méně než nula být nemůže")
elif cas<5:
    print(f"je noc")
elif cas<=9:
    print("je ráno")
elif cas<12: 
    print("je dopoledne")
elif cas==12: 
    print("je poledne")
elif cas<18:
    print("je odpoledne")
elif cas<=20:
    print("je večer")
elif cas<24:
    print("je noc")
elif cas>23:
    print("tolik hodin neexistuje")