import random as rnd
import csv
import numpy as np


def create_generation(pocet_mest, mnozstvi_jedincu, start_city):
    """
    Vytvoření počáteční generace(populace)
    :param pocet_mest: Počet měst v matici
    :param mnozstvi_jedincu: Kolik jedinců chceme
    :param start_city: Začátek cesty
    :return:  Seznam obsahující jedincy,představující sebou jednotlivé seznamy s náhodně promichanými čísly
    """

    cisla = list()    # cisla je seznam cisel jdoucich od 1 do M
    for i in range(1, pocet_mest + 1):
        cisla.append(i)

    generace = []

    for i in range(mnozstvi_jedincu):
        generace.append(rnd.sample(cisla, len(cisla)))    # nahodne promichame cisla a dame do seznamu
        generace[i].remove(start_city)     # delece pocatku cesty
        generace[i].insert(0, start_city)    # pridame zacatek cesty na prvni

    return generace


def crossingover(jedinec):     # [1,2,4,6,3,5]
    """
    Náhodně promíchání části řetezce
    :param jedinec: Posloupnost cisel
    :return: Zkrosingovany jedinec

    Dodat/rozšířit:
    -Pro celou generaci, ted' jenom pro jednoho.
    -Vstupem je taky pravděpodobnosti prošle do další generace.
    -Pokud došlo ke křížení u jedincu, on se přída do další generace. A co so starým? Zmízí se nebo se přidá taky?
    """
    index_1 = rnd.randint(1, len(jedinec))    # urcujeme indexy odkud a dokud budeme michat, do pocatecniho mesta nezasahujeme (neni smysl)
    index_2 = rnd.randint(1, len(jedinec))

    while index_1 == index_2:    # aby to nebylo stejne cislo, potrebujeme retezec
        index_1 = rnd.randint(1, len(jedinec))
        index_2 = rnd.randint(1, len(jedinec))

    if index_1 > index_2:
        index_1, index_2 = index_2, index_1    # index_1 bude vzdy mensi nez index_2

    new_jedinec = jedinec[:index_1]
    michana_cast = rnd.sample(jedinec[index_1:index_2 + 1], len(jedinec[index_1:index_2 + 1]))
    new_jedinec.extend(michana_cast)
    new_jedinec.extend(jedinec[index_2 + 1:])

    return new_jedinec


def mutation(jedinec):    # [1,2,4,6,3,5]
    """
    Nahodne prohozeni dvou cisel v posloupnosti jedincu.
    Dodat/rozšířit:
    -Pro celou generaci, ted' jenom pro jednoho.
    -Vstupem je taky pravděpodobnosti prošle do další generace.
    -Pokud došlo k mutaci u jedincu, on se přída do další generace, a co so starým? Zmízí nebo se přidá taky?
    :param jedinec: Posloupnost cisel
    :return: Zmutovany jedinec
    """
    index_1 = rnd.randint(1, len(jedinec) - 1)
    index_2 = rnd.randint(1, len(jedinec) - 1)

    while index_1 == index_2:
        index_1 = rnd.randint(1, len(jedinec) - 1)
        index_2 = rnd.randint(1, len(jedinec) - 1)

    jedinec[index_1], jedinec[index_2] = jedinec[index_2], jedinec[index_1]

    return jedinec


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
    :return: Seznam délek cest jednotlivých jedinců, indexy jsou shodé, první v seznamu odpovidá prvnímu v generace
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
    Transformace kvalit(délek cest) do pravděpodobnosti pro vyhození z generace.
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


def selection(probabilities, generation):
    """
    Na zakladě pravděpodobnosti určuje kdo projde do další generace.
    :param probabilities:
    :param generation:
    :return:
    """
    i = 0
    b = 0
    dl = len(probabilities)    # řídí cykl

    while b != dl:
        var = rnd.random()    # rand float od 0 do 1
        pom = var - probabilities[i]    # pomocná proměnná
        if pom <= 0:
            del probabilities[i]
            del generation[i]
            b += 1
        else:
            i += 1
            b += 1

    return probabilities, generation