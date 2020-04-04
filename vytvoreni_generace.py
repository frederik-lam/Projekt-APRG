import random

mnozstvi_jedincu = int(input("Zadejte mnozstvi potřebných jedincu: "))

def vytvoreni_generace(sezn_cisel, mnozstvi_jedincu):
    """
    vytvari seznam obsahujici jednotlive seznamy s nahodne promichanymi cisly, predstavujici jedincy
    :param sezn_cisel: seznam cisel od 1 do M(mnozstvi mest)
    :param mnozstvi_jedincu: zadejme kolik jedincu budeme chtit v generace, ktera pak se bude menit ale mnozstvi jedincu ne.
    :return:
    """
    generace = []
    for i in range(mnozstvi_jedincu):
        generace.append(random.sample(sezn_cisel, len(sezn_cisel)))

    return generace, print(generace)

def main():

    vytvoreni_generace([1,2,3,4,5], mnozstvi_jedincu)

if __name__ == "__main__":
    main()

