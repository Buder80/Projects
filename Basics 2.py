def czysc(ubranie):
    czyste_ubranie = ubranie.replace("brudne", "czyste")
    czyste_ubranie = czyste_ubranie.replace("brudna", "czysta")
    return czyste_ubranie

def pralka(*args, proszek):
    print(f"uzywam proszku {proszek}")
    czyste_ubrania = []
    for ubranie in args:
        czyste_ubrania.append(czysc(ubranie))

    return czyste_ubrania

brudne_ciuchy = [
    "brudne skarpetki",
    "brudne spodnie",
    "brudna koszulka"
]


wynik = pralka(*brudne_ciuchy, proszek="od chajzera")
print(wynik)

