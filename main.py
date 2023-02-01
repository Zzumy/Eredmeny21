"""megoldás"""


def eredmeny():

    """tesztesetek"""
    jatekosPontjai = 2
    gepPontjai = 3
    
    if jatekosPontjai > 21:
        print("Játékos vesztett.")
    elif gepPontjai > 21:
        print("Gép vesztett.")
    elif 21 >= jatekosPontjai > gepPontjai:
        print("Játékos nyert.")
    elif 21 >= gepPontjai > jatekosPontjai:
        print("Gép nyert.")

