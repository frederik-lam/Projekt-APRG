import csv
import numpy as np


def file_read():
    """
    Nacteni csv souboru s daty, overovani spravneho formatu, vytvoreni matice(array).
    a musime dodat:

    :return: Matice hodnoceni delek cest mezi mesty, pocet mest
    Dodat/rozšířit:
    -Kontrolu záporných hodnot ve datach
    -Načtení ostatních formátu než jenom csv (knihovna xlrd)
    -Jaké vůbec další formáty potřebujeme
    """
    formaty = ["csv", "xls", "xlsx"]
    nazev = "data_vzdalenosti.csv"
    # nazev = input("Napiste nazev souboru bez uvazovok: ")
    soubor = nazev.split('.')

    if len(soubor) >= 2:
        file_format = soubor[-1].lower()
        if file_format not in formaty:
            return False, print("Spatne zadany format souboru")
    else:
        print("Napiste jmeno souboru s pozadovanym formatem")
        file_read()

    new_list = []

    with open(nazev, newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";", quotechar="|")
        for i in csv_reader:
            new_list.append(i)

    mat = np.array(new_list)
    pocet_mest = len(mat[0])

    # if mat_hod.any() < 0:
        # print("Data nesmi obsahovat zaporna cisla")

    return mat, pocet_mest


def quality(generace, mat_hod):
    """
    Určuje kvalitu generace(délku cest)
    :param generace: Seznam s jedinci
    :param mat_hod: Matice, zpracovana data
    :return: Seznam délek cest jednotlivých jedinců, první index v seznamu odpovidá prvnímu v generace
    """
    kvality = []
    for j in generace:
        kval = 0
        for i in range(len(j) - 1):
            kval += int(mat_hod[j[i] - 1][j[i + 1] - 1])
        kval += int(mat_hod[j[0] - 1][j[-1] - 1])
        kvality.append(kval)

    return kvality


def qual_to_prob(kvality):
    """
    Transformace kvalit(délek cest) do pravděpodobnosti pro vyhození z delka_generace.
    Nejkratší cesta = 0 pravdepodobnost, největší = 1.
    :param kvality:
    :return:
    """
    pravd = []
    arr = np.array(kvality)
    max_cislo = max(arr)

    if max_cislo < 10:
        pravd = arr / 10
    elif max_cislo < 100:
        pravd = arr / 100
    elif max_cislo < 1000:
        pravd = arr / 1000
    elif max_cislo < 10000:
        pravd = arr / 10000
    elif max_cislo < 100000:
        pravd = arr / 100000
    elif max_cislo < 1000000:
        pravd = arr / 1000000

    probabilities_arr = pravd - min(pravd)    # vycitame nejmensi
    probabilities_arr = probabilities_arr / max(probabilities_arr)    # pak vydelime nejvetsim
    probabilities_list = np.ndarray.tolist(probabilities_arr)    # prevadime do listu

    return probabilities_list