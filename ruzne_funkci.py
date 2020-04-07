from random import sample
from random import randint
import csv
import numpy as np

def create_generation(pocet_mest, mnozstvi_jedincu, start_city):
    """
    vytvari seznam obsahujici jedincy,predstavujici sebou jednotlive seznamy s nahodne promichanymi cisly, se stejnym zacatkem.
    :param sezn_cisel: seznam cisel od 1 do M(mnozstvi mest)
    :param mnozstvi_jedincu: zadejme kolik jedincu budeme chtit v generace, ktera pak se bude menit ale mnozstvi jedincu ne.
    :return:
    """
    cisla = list()  # cisla je seznam cisel jdoucich od 1 do M, ktery budeme vyuzivat ve vytvoreni generace a jedincu tam nachazeicich
    for i in range(1, pocet_mest + 1):
        cisla.append(i)

    generace = []

    for i in range(mnozstvi_jedincu):
        generace.append(sample(cisla, len(cisla)))
        generace[i].remove(start_city)
        generace[i].insert(0, start_city)

    return generace



def crossingover(jedinec):
    """
    nahodne promichani casti retezce
    :param jedinec: posloupnost cisel
    :return:
    """

    index_1 = randint(1, len(jedinec)) #urcujeme indexy odkud a dokud budeme michat
    index_2 = randint(1, len(jedinec))

    while index_1 == index_2: #aby to nebylo samotne cislo, potrebujeme retezec
        index_1 = randint(1, len(jedinec))
        index_2 = randint(1, len(jedinec))

    if index_1 > index_2:
        index_1, index_2 = index_2, index_1 #index_1 bude vzdy mensi nez index_2

    new_jedinec = jedinec[:index_1]
    michana_cast = sample(jedinec[index_1:index_2 + 1], len(jedinec[index_1:index_2 + 1]))
    new_jedinec.extend(michana_cast)
    new_jedinec.extend(jedinec[index_2 + 1:])

    return new_jedinec



def mutation(jedinec):
    """
    nahodne prohozeni dvou cisel v posloupnosti
    :param jedinec: posloupnost cisel
    :return:
    """
    index_1 = randint(1, len(jedinec) - 1)
    index_2 = randint(1, len(jedinec) - 1)

    jedinec[index_1], jedinec[index_2] = jedinec[index_2], jedinec[index_1]

    return jedinec



def nacteni_souboru(nazev):
    # nacteni csv souboru s daty
    new_list = []
    with open(nazev, newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";", quotechar="|")
        for i in csv_reader:
            new_list.append(i)

    # delame z nej matice
    mat = np.array(new_list)
    # zjistujeme mnozstvi mest
    M = len(mat[1])

    return mat, M


def urceni_kvality(generace, mat):

    kvality = []
    for j in generace:
        kval = 0
        for i in range(len(j) - 1):
            kval += int(mat[j[i] - 1][j[i + 1] - 1])
        kval += int(mat[j[0] - 1][j[-1] - 1])
        kvality.append(kval)

    return kvality
