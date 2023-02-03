"""------------------------------------------------------------------------------------------------------------------"""
"""----------------------------------------------------MEGOLDÁS------------------------------------------------------"""
"""------------------------------------------------------------------------------------------------------------------"""


def eredmeny(jatekoslapok, geplapok):

    szoveg = ""
    jatekos = pontszamitas(jatekoslapok)
    gep = pontszamitas(geplapok)

    if jatekos > 21:
        szoveg = "Játekos vesztett"
    elif gep > 21:
        szoveg = "Gép vesztett"
    return szoveg

def pontszamitas(lapok):

    index = 0
    pontok = 0
    while index < len(lapok):
        pontok += lapok[index]
        index += 1
    return pontok


"""------------------------------------------------------------------------------------------------------------------"""
"""----------------------------------------------------TESZTESETEK---------------------------------------------------"""
"""------------------------------------------------------------------------------------------------------------------"""


def jatekosVesztettTesztElso():

    jatekosLista = [10, 10, 10]
    gepLista = [10, 5, 5]
    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    # játékos meghaladja a 21-et
    vartEredmeny = "Játekos vesztett"

    if kapottEredmeny == vartEredmeny:
        print("Teszt sikeres. :)")
    else:
        print("Teszt megbukott. :(")


def jatekosVesztettTesztMasodik():

    jatekosLista = [10, 5, 4]
    gepLista = [10, 5, 5]
    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    # gép közelebb áll a 21-hez
    vartEredmeny = "Játekos vesztett"

    if kapottEredmeny == vartEredmeny:
        print("Teszt sikeres. :)")
    else:
        print("Teszt megbukott. :(")


def gepVesztettTesztElso():

    jatekosLista = [10, 5, 5]
    gepLista = [10, 10, 10]
    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    # gép meghaladja a 21-et
    vartEredmeny = "Gép vesztett"

    if kapottEredmeny == vartEredmeny:
        print("Teszt sikeres. :)")
    else:
        print("Teszt megbukott. :(")


def gepVesztettTesztMasodik():

    jatekosLista = [10, 5, 5]
    gepLista = [10, 5, 4]
    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    # játékos közelebb áll a 21-hez
    vartEredmeny = "Gép vesztett"

    if kapottEredmeny == vartEredmeny:
        print("Teszt sikeres. :)")
    else:
        print("Teszt megbukott. :(")


def mindkettoVeszitTeszt():

    jatekosLista = [10, 10, 10]
    gepLista = [10, 10, 10]
    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    # játékos és gép pontjainak száma meghaladja a 21-et
    vartEredmeny = "Gép vesztett"

    if kapottEredmeny == vartEredmeny:
        print("Teszt sikeres. :)")
    else:
        print("Teszt megbukott. :(")


def jatekosGepDontetlen():

    jatekosLista = [10, 10, 4]
    gepLista = [10, 10, 4]
    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    # játékos és gép pontjainak száma megeggyezik
    vartEredmeny = "Gép vesztett"

    if kapottEredmeny == vartEredmeny:
        print("Teszt sikeres. :)")
    else:
        print("Teszt megbukott. :(")


def tesztek():
    jatekosVesztettTesztElso()
    jatekosVesztettTesztMasodik()
    gepVesztettTesztElso()
    gepVesztettTesztMasodik()
    mindkettoVeszitTeszt()
    jatekosGepDontetlen()


tesztek()
