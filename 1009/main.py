# vyhodnocení kolize

#kolizní doména
x1 = 2
y1 = 1.5
x2=6
y2=7

xb=float (input("zadej x souřadnici panáčka"))
yb=float (input("zadej y souřadnici panáčka"))
if xb>=x1 and xb<=x2 and yb>=y1 and yb<=y2:
    print("kolize bodu s obdelníkem")
else: 
    print ("bez kolize")

if xb<x1 or xb>x2 or yb<y1 or yb>y2:
    print("kolize bodu s obdelníkem")
else: 
    print("kolize bodu s obdelníkem")
    