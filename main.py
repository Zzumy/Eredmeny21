"""megoldás"""


def eredmeny(jatekoslapok, geplapok):

    jatekos = pontszamitas(jatekoslapok)
    gep = pontszamitas(geplapok)

    if jatekos > 21:
        print("Jatekos vesztett")
    elif gep > 21:
        print("Gep vesztett")


def pontszamitas(lapok):

    index = 0
    pontok = 0
    while index < lapok:
        pontok =+ lapok[index]
        index += 1
    return pontok

"""tesztesetek"""
