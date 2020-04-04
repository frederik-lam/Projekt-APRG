from random import sample

def create_generation(sezn_cisel, mnozstvi_jedincu):
    """
    vytvari seznam obsahujici jednotlive seznamy s nahodne promichanymi cisly, predstavujici jedincy
    :param sezn_cisel: seznam cisel od 1 do M(mnozstvi mest)
    :param mnozstvi_jedincu: zadejme kolik jedincu budeme chtit v generace, ktera pak se bude menit ale mnozstvi jedincu ne.
    :return:
    """
    generace = []
    for i in range(mnozstvi_jedincu):
        generace.append(sample(sezn_cisel, len(sezn_cisel)))

    return generace, print(generace)


