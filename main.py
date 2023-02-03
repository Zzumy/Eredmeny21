"""megoldás"""


def eredmeny(jatekoslapok, geplapok):

    szoveg = ""
    jatekos = pontszamitas(jatekoslapok)
    gep = pontszamitas(geplapok)

    if jatekos > 21:
        szoveg = "Jatekos vesztett"
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

"""tesztesetek"""

def jatekosVesztettTeszt():

    jatekosLista = [6, 4, 8, 9]
    gepLista = [6, 4, 11]
    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Jatekos vesztett"

    if kapottEredmeny == vartEredmeny:
        print("Teszt sikeres. :)")
    else:
        print("Teszt megbukott. :(")


def jatekosVesztettTeszt2():

    jatekosLista = [10, 5, 5]
    gepLista = [10, 10, 10]
    kapottEredmeny = eredmeny(jatekosLista, gepLista)
    vartEredmeny = "Gép vesztett"

    if kapottEredmeny == vartEredmeny:
        print("Teszt sikeres. :)")
    else:
        print("Teszt megbukott. :(")

def tesztek():
    jatekosVesztettTeszt2()


tesztek()
