#Przemyslaw Budrewicz
#16/09/22
#Papier Kamien Nozyczki


gracz1_wynik = 0
gracz2_wynik = 0

opcje = ["papier", "Papier", "kamien", "Kamien", "nozyczki", "Nozyczki"]
print("Gra w papier, kamien, nozyczki.")



def pobierz_wybor(gracz):
    while True:
        wybor_gracza = input(f'{gracz} podaj swoj wybor: ')
        if wybor_gracza in opcje:
            return wybor_gracza

def sprawdz_wynik(wybor_gracza1, wybor_gracza2):
    if wybor_gracza1 == wybor_gracza2:
        print("Remis")
        return 0

    wynik = {
        ("papier", "kamien"): 1,
        ("kamien", "nozyczki"): 1,
        ("nozyczki", "papier"): 1
    }

    return wynik.get((wybor_gracza1, wybor_gracza2), -1)

while gracz1_wynik != 3 and gracz2_wynik != 3:
    wybor_gracza1 = pobierz_wybor("Gracz1")
    wybor_gracza2 = pobierz_wybor("Gracz2")
    wynik = sprawdz_wynik(wybor_gracza1, wybor_gracza2)

    if wynik == 1:
        print("Wygral gracz1")
        gracz1_wynik += 1
    elif wynik == -1:
        print("Wygral gracz 2")
        gracz2_wynik += 1



if gracz1_wynik > gracz2_wynik:
    print("Cala gre wygral Gracz 1")
else:
    print("Cala gre wygral Gracz 2")