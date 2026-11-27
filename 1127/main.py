def cifra(cislo):
    if cislo==10:
        return "A"
    elif cislo==11:
        return "B"
    elif cislo==12:
            return "C"
    elif cislo==13:
            return "D"
    elif cislo==14:
            return "E"
    elif cislo==15:
            return "F"
    else: return str(cislo)


def fromDec(cislo, zaklad):
    prevedene_cislo=""
    while cislo>0:
        zbytek=cislo%zaklad
        cislo//=zaklad
        prevedene_cislo=cifra(zbytek)+prevedene_cislo
    return prevedene_cislo

maximum=int(input("zadej číslo: "))
print("DEC      BIN      OCT     HEX")
print("-----------------------------")
print(fromDec(6,2)) #prevedu na dvojkove cislo
print(fromDec(255,16)) #prevedu na HEX cislo
