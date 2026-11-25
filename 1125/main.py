# Kreslení obrazců z hvězdiček (krátká verze). Hvězdičky se kreslí jen cyklem while,
# řádek se skládá násobením řetězce. Při neplatném rozměru (<= 0) funkce vrací None.

import unicodedata  # pro odstranění diakritiky ze vstupu


def obdelnik(a, b, vyplneny=True):
    """Obdélník a x b (šířka x výška); čtverec = stejné a, b."""
    if a <= 0 or b <= 0:
        return None
    radky = []
    i = 0
    while i < b:
        if vyplneny or i == 0 or i == b - 1:
            radky.append("*" * a)                    # plný řádek (vyplněný nebo horní/dolní strana)
        else:
            radky.append(("*" + " " * (a - 2) + "*")[:a])  # jen okraje, [:a] ošetří šířku 1
        i += 1
    return "\n".join(radky)


def trojuhelnik_levy(z):
    """Řádek i má i hvězdiček zarovnaných vlevo."""
    if z <= 0:
        return None
    radky = []
    i = 1
    while i <= z:
        radky.append("*" * i)
        i += 1
    return "\n".join(radky)


def trojuhelnik_pravy(z):
    """Řádek i má (z - i) mezer a pak i hvězdiček (zarovnání vpravo)."""
    if z <= 0:
        return None
    radky = []
    i = 1
    while i <= z:
        radky.append(" " * (z - i) + "*" * i)
        i += 1
    return "\n".join(radky)


def trojuhelnik_rovnoramenny(z):
    """Každý řádek je o 2 hvězdičky širší; lichá základna začíná 1, sudá 2 hvězdičkami."""
    if z <= 0:
        return None
    radky = []
    h = 1 if z % 2 == 1 else 2                       # počet hvězdiček v prvním řádku
    while h <= z:
        radky.append(" " * ((z - h) // 2) + "*" * h)  # odsazení vycentruje řádek
        h += 2
    return "\n".join(radky)


def cislo(text):
    """Načte celé číslo; při chybě vrátí 0 (= neplatný rozměr)."""
    try:
        return int(input(text))
    except ValueError:
        return 0


def uprav(text):
    """Převede vstup na malá písmena bez diakritiky a nadbytečných mezer,
    aby šlo psát 'čtverec' i 'ctverec'."""
    text = unicodedata.normalize("NFD", text.lower())
    text = "".join(z for z in text if unicodedata.category(z) != "Mn")
    return " ".join(text.split())


def main():
    print("VÍTEJ V PROGRAMU PRO KRESLENÍ GEOMETRICKÝCH TVARŮ")
    print("Obrazce: čtverec, obdélník, nevyplněný čtverec, nevyplněný obdélník,")
    print("         levý trojúhelník, pravý trojúhelník, rovnoramenný trojúhelník")
    dalsi = "ano"
    while dalsi == "ano":
        volba = uprav(input("Jaký obrazec chceš vykreslit? "))
        if volba in ("obdelnik", "nevyplneny obdelnik"):
            obr = obdelnik(cislo("Jak dlouhá je strana a? "), cislo("Jak dlouhá je strana b? "),
                           volba == "obdelnik")
        elif volba in ("ctverec", "nevyplneny ctverec"):
            a = cislo("Jak velká má být jeho strana? ")
            obr = obdelnik(a, a, volba == "ctverec")
        elif volba == "levy trojuhelnik":
            obr = trojuhelnik_levy(cislo("Jak vysoký má být? "))
        elif volba == "pravy trojuhelnik":
            obr = trojuhelnik_pravy(cislo("Jak vysoký má být? "))
        elif volba == "rovnoramenny trojuhelnik":
            obr = trojuhelnik_rovnoramenny(cislo("Jak dlouhá má být základna? "))
        else:
            obr = "Neznámý obrazec, zkus jeden z nabídky."
        print(obr if obr else "Neplatný rozměr - zadej celé číslo větší než 0.")
        dalsi = uprav(input("Chceš vykreslit další obrazec? "))
    print("DĚKUJI ZA POUŽITÍ PROGRAMU")


if __name__ == "__main__":
    main()