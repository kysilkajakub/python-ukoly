import urllib.request
url="https://voskh.cz/envirotyden/index.php?lokalita=kutnahora"

urllib.request.urlopen(url)

radek=odpoved.readline()

while bool(radek):
    text_radku=radek.decode("utf-8")
    denni_srazky=float(text_radku)
    if denni_srazky>=0:
        celkem_srazky += 1
    radek=odpoved.readline()

while
odpoved.close()
print(celkem_srazky/pocet_dni)