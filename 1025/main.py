a=int(input("zadej prvni cislo"))
b=int(input("zadej druhe cislo")) 
c=int(input("zadej treti cislo"))
min=a
max=a
if b<min:
    b=min
elif b>max:
   max=b
if c<min:
    min=c
elif c>max:
    max=c

print(f"Minimum: {min}\nMaximum:{max}")