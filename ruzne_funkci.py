import random as rnd
import csv
import numpy as np


def create_generation(pocet_mest, mnozstvi_jedincu, start_city):
    """
    Vytvoreni pocatecni generace(populace)
    :param pocet_mest: Pocet mest v matici
    :param mnozstvi_jedincu: Kolik jedincu chceme
    :param start_city: Zacatek cesty
    :return:  Seznam obsahujici jedincy,predstavujici sebou jednotlive seznamy s nahodne promichanymi cisly
    """
    cisla = list()    # cisla je seznam cisel jdoucich od 1 do M
    for i in range(1, pocet_mest + 1):
        cisla.append(i)

    generace = []

    for i in range(mnozstvi_jedincu):
        generace.append(rnd.sample(cisla, len(cisla)))
        generace[i].remove(start_city)
        generace[i].insert(0, start_city)

    return generace


def crossingover(jedinec):
    """
    Nahodne promichani casti retezce
    :param jedinec: Posloupnost cisel
    :return: Zkrosingovany jedinec
    """
    index_1 = rnd.randint(1, len(jedinec))    # urcujeme indexy odkud a dokud budeme michat
    index_2 = rnd.randint(1, len(jedinec))

    while index_1 == index_2:    # aby to nebylo samotne cislo, potrebujeme retezec
        index_1 = rnd.randint(1, len(jedinec))
        index_2 = rnd.randint(1, len(jedinec))

    if index_1 > index_2:
        index_1, index_2 = index_2, index_1    # index_1 bude vzdy mensi nez index_2

    new_jedinec = jedinec[:index_1]
    michana_cast = rnd.sample(jedinec[index_1:index_2 + 1], len(jedinec[index_1:index_2 + 1]))
    new_jedinec.extend(michana_cast)
    new_jedinec.extend(jedinec[index_2 + 1:])

    return new_jedinec


def mutation(jedinec):
    """
    Nahodne prohozeni dvou cisel v posloupnosti
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
    Nacteni csv souboru s daty, overovani spravneho formatu, a musime dodat kontrolu zapornych hodnot ve datach
    :return: Matice, pocet mest
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

    # if mat.any() < 0:
        # print("Data nesmi obsahovat zaporna cisla")

    return mat, pocet_mest


def quality(generace, mat):
    """
    Urcuje kvalitu generace(delku cest)
    :param generace: Seznam s jedinci
    :param mat: Matice, zpracovana data
    :return: Seznam delek cest jednotlivych jedincu, indexy jsou shode, prvni v seznamu odpovidaji prvnimu v generace
    """
    kvality = []
    for j in generace:
        kval = 0
        for i in range(len(j) - 1):
            kval += int(mat[j[i] - 1][j[i + 1] - 1])
        kval += int(mat[j[0] - 1][j[-1] - 1])
        kvality.append(kval)

    return kvality


def qual_to_prob(kvality):
    """
    Transformace kvalit do pravdepodobnosti, roztazene od 0 do 1.
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

    probabilities_arr = pravd - min(pravd)
    probabilities_arr = probabilities_arr / max(probabilities_arr)
    probabilities_list = np.ndarray.tolist(probabilities_arr)

    return probabilities_list


def selection(probs, generation):

    i = 0
    b = 0
    dl = len(probs)

    while b != dl:
        var = rnd.random()
        pom = var - probs[i]
        if pom <= 0:
            del probs[i]
            del generation[i]
            b += 1
        else:
            i += 1
            b += 1

    return probs, generation