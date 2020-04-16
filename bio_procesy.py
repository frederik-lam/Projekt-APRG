import random as rnd
import numpy as np


def create_generation(pocet_mest, mnozstvi_jedincu, start_city):
    """
    Vytvoření počáteční delka_generace(populace)
    :param pocet_mest: Počet měst v matici
    :param mnozstvi_jedincu: Kolik jedinců chceme
    :param start_city: Začátek cesty
    :return:  Seznam obsahující jedincy,představující sebou jednotlivé seznamy s náhodně promichanými čísly
    """

    cisla = list()  # cisla je seznam cisel jdoucich od 1 do pocet_mest
    for i in range(1, pocet_mest + 1):
        cisla.append(i)

    generace = []

    for i in range(mnozstvi_jedincu):
        generace.append(rnd.sample(cisla, len(cisla)))  # nahodne promichame cisla a dame do seznamu
        generace[i].remove(start_city)  # delece pocatku cesty
        generace[i].insert(0, start_city)  # pridame zacatek cesty na prvni

    return generace


def crossingover(generace, probs, mnozstvi_jedincu):  # [1,2,4,6,3,5]
    """
    Náhodně promíchání části řetezce
    :param generace: Seznam jedincu
    :param probs: Seznam pravděpodobnosti
    :param mnozstvi_jedincu: Kolik jedincu musi byt v generace
    :return: Zkrosingovany jedinec
    """
    new_generace = []
    delka_generace = len(generace)
    delka_jedincu = len(generace[0])
    probs_arr = np.array(probs)
    probs_arr = probs_arr / max(probs_arr)  # zvyrazneni prvku lisicich se od nejlepsiho(0)

    for i in range(delka_generace):
        if mnozstvi_jedincu > len(new_generace):
            var = rnd.random()
            if var - probs_arr[i] < 0:
                index_1 = int(delka_jedincu / 2)  # od tohoto indexu
                index_2 = delka_jedincu  # do tohoto

                new_jedinec = generace[i][:index_1]
                michana_cast = rnd.sample(generace[i][index_1:index_2 + 1], len(generace[i][index_1:index_2 + 1]))
                new_jedinec.extend(michana_cast)
                new_generace.append(new_jedinec)  # do nove generace jde zkrossingovany jedinec
            else:
                new_generace.append(generace[i])
        else:
            break

    return new_generace, probs_arr


def mutation(generace):  # [1,2,4,6,3,5]
    """
    Nahodne prohozeni dvou cisel v posloupnosti jedincu.
    Dodat/rozšířit:
    -Vstupem je taky pravděpodobnosti prošle do další delka_generace.
    :param generace: Generacia jedincov, ktora bude mutovana
    :return: mutovana_generace: Generacia po mutacii
    """
    mutovana_generace = []
    for jedinec in generace:
        delka_jed = len(jedinec)
        [index_1, index_2] = rnd.sample(range(delka_jed),2) # nahodny vyber 2 prvkov
        jedinec[index_1], jedinec[index_2] = jedinec[index_2], jedinec[index_1] #prehodenie danych prvkov
        mutovana_generace.append(jedinec)

    return mutovana_generace


def selection(generation, probabilities):
    """
    Na zakladě pravděpodobnosti určuje kdo projde do další delka_generace.
    :param probabilities:
    :param generation:
    :return:
    """
    i = 0
    b = 0
    dl = len(probabilities)  # řídí cykl

    while b != dl:
        var = rnd.random()  # rand float od 0 do 1
        if var - probabilities[i] < 0:
            del probabilities[i]
            del generation[i]
            b += 1
        else:
            i += 1
            b += 1

    return generation, probabilities
