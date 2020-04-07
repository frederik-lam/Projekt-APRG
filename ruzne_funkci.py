from random import sample
from random import randint
import csv
import numpy as np

def create_generation(pocet_mest, mnozstvi_jedincu, start_city):
    """
    :param pocet_mest: Pocet mest v matici
    :param mnozstvi_jedincu: Kolik jedincu chceme
    :param start_city: Zacatek cesty
    :return:  Seznam obsahujici jedincy,predstavujici sebou jednotlive seznamy s nahodne promichanymi cisly
    """
    cisla = list()  # cisla je seznam cisel jdoucich od 1 do M
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
    Nahodne promichani casti retezce
    :param jedinec: Posloupnost cisel
    :return: Zkrosingovany jedinec
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
    Nahodne prohozeni dvou cisel v posloupnosti
    :param jedinec: Posloupnost cisel
    :return: Zmutovany jedinec
    """
    index_1 = randint(1, len(jedinec) - 1)
    index_2 = randint(1, len(jedinec) - 1)

    jedinec[index_1], jedinec[index_2] = jedinec[index_2], jedinec[index_1]

    return jedinec



def nacteni_souboru(nazev):
    """
    Nacteni csv souboru s daty
    :param nazev: Bez uvazovok nazev souboru, ktery lezi ve stejne slozce se hlavnim skriptem
    :return: Matice, pocet mest
    """
    new_list = []
    with open(nazev, newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";", quotechar="|")
        for i in csv_reader:
            new_list.append(i)

    mat = np.array(new_list)

    M = len(mat[1])

    return mat, M


def urceni_kvality(generace, mat):
    """
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
