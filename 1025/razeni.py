a=int(input("zadej prvni cislo"))
b=int(input("zadej druhe cislo"))
c=int(input("zadej treti cislo"))
if a>b:
    p=a
    a=b
    b=p
if b>c:
    p=b
    b=c
    c=p
if a>b:
    p=a
    a=b
    b=p
print (f"{a}<{b}<{c}")