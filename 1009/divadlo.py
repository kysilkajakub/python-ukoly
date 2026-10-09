zaklad:500
vek=float (input ("kolik vám je let:"))
student=float (input("jste student (ano/ne):"))
pocet=float (input("počet osob"))
if pocet>=4:
    sleva=25
    typ_slevy= "sleva 25%"
elif= vek<26 and student =="ano":
    sleva:30
    typ_slevy= "sleva 30%"
elif= vek>=65:
    sleva=20
    typ_slevy= "sleva 20%" 
else:
    sleva=0
    typ_slevy="bez slevy"

    cena_po_sleve=cena* (1-sleva/100)
    celkem=cena_po_sleve
    print("typ slevy:", typ_slevy)
    print("cena za jednu vstupenku", cena_po_sleve)
    print("celková cena", celkem)


