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


def jatekos_vesztett_teszt_elso():

    jatekos_lista = [10, 10, 10]
    gep_lista = [10, 5, 5]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    # játékos meghaladja a 21-et
    vart_eredmeny = "Játekos vesztett"

    if kapott_eredmeny == vart_eredmeny:
        print("Teszt sikeres. :)")
    else:
        print("Teszt megbukott. :(")


def jatekos_vesztett_teszt_masodik():

    jatekos_lista = [10, 5, 4]
    gep_lista = [10, 5, 5]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    # gép közelebb áll a 21-hez
    vart_eredmeny = "Játekos vesztett"

    if kapott_eredmeny == vart_eredmeny:
        print("Teszt sikeres. :)")
    else:
        print("Teszt megbukott. :(")


def gep_vesztett_teszt_elso():

    jatekos_lista = [10, 5, 5]
    gep_lista = [10, 10, 10]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    # gép meghaladja a 21-et
    vart_eredmeny = "Gép vesztett"

    if kapott_eredmeny == vart_eredmeny:
        print("Teszt sikeres. :)")
    else:
        print("Teszt megbukott. :(")


def gep_vesztett_teszt_masodik():

    jatekos_lista = [10, 5, 5]
    gep_lista = [10, 5, 4]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    # játékos közelebb áll a 21-hez
    vart_eredmeny = "Gép vesztett"

    if kapott_eredmeny == vart_eredmeny:
        print("Teszt sikeres. :)")
    else:
        print("Teszt megbukott. :(")


def mindketto_veszit_teszt():

    jatekos_lista = [10, 10, 10]
    gep_lista = [10, 10, 10]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    # játékos és gép pontjainak száma meghaladja a 21-et
    vart_eredmeny = "Gép vesztett"

    if kapott_eredmeny == vart_eredmeny:
        print("Teszt sikeres. :)")
    else:
        print("Teszt megbukott. :(")


def jatekos_gep_dontetlen():

    jatekos_lista = [10, 10, 4]
    gep_lista = [10, 10, 4]
    kapott_eredmeny = eredmeny(jatekos_lista, gep_lista)
    # játékos és gép pontjainak száma megeggyezik
    vart_eredmeny = "Gép vesztett"

    if kapott_eredmeny == vart_eredmeny:
        print("Teszt sikeres. :)")
    else:
        print("Teszt megbukott. :(")


def tesztek():
    jatekos_vesztett_teszt_elso()
    jatekos_vesztett_teszt_masodik()
    gep_vesztett_teszt_elso()
    gep_vesztett_teszt_masodik()
    mindketto_veszit_teszt()
    jatekos_gep_dontetlen()


tesztek()
