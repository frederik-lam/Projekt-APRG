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


def selekcia(generation, probs):
    """
    Na zakladě pravděpodobnosti určuje kdo projde do další_generace.
    :param generation:
    :return selected_breeder: Jedinec, ktory bude mat sancu sa krizit
    """

    new_generation = []
    kolik = len(generation)

    while len(new_generation) != kolik:
        for i in range(len(probs)):
            var = rnd.random()
            if probs[i] - var > 0:
                new_generation.append(generation[i])
                break

    return new_generation


def crossingover(generace):  # [1,2,4,6,3,5]
    """
    Náhodně promíchání části řetezce
    :param generace: Seznam jedincu
    :return: Zkrosingovany jedinec
    """
    delka_generace = len(generace)
    delka_jedincu = len(generace[0])
    index_1 = 0
    index_2 = 0

    for i in range(delka_generace):  # budeme jit ke kazdemu
        pom = 0.8
        var = rnd.random()
        if pom - var < 0:
            while index_1 == index_2:
                index_1 = rnd.randint(1, delka_jedincu)     # od tohoto indexu
                index_2 = rnd.randint(1, delka_jedincu)    # do tohoto
            if index_1 > index_2:
                [index_1, index_2] = [index_2, index_1]

            new_jedinec = generace[i][:index_1]
            michana_cast = rnd.sample(generace[i][index_1:index_2 + 1], len(generace[i][index_1:index_2 + 1]))
            new_jedinec.extend(michana_cast)
            new_jedinec.extend(generace[i][index_2+1:])
            generace.pop(i)
            generace.insert(i, new_jedinec)    # do nove generace jde zkrossingovany jedinec

    return generace


def mutation(generace):  # [1,2,4,6,3,5]
    """
    Nahodne prohozeni dvou cisel v posloupnosti jedincu.
    :param generace: Generacia jedincov, ktora bude mutovana
    :return: mutovana_generace: Generacia po mutacii
    """
    gen_length = len(generace)
    num_of_mutauions = rnd.randint(0, gen_length-1)  # nahodny vyber poctu mutovanych jedincov
    mutated_individuals = rnd.sample(range(1, gen_length), num_of_mutauions)  # nahodny vyber jedincov u
    # ktorych dojde k mutacii, mimo najlepsieho jedinca, ktory je na 1. mieste
    for i in mutated_individuals:
        jedinec = generace[i]
        generace.pop(i)  # odstranenie jedinca y povodnej generacie
        delka_jed = len(jedinec)
        [index_1, index_2] = rnd.sample(range(1, delka_jed), 2)  # nahodny vyber 2 prvkov, vynechanie startovacieho mesta
        jedinec[index_1], jedinec[index_2] = jedinec[index_2], jedinec[index_1]  # prehodenie danych prvkov
        generace.insert(i, jedinec)  # vratenie mutovaneho jedinca na povodnu poziciu

    mutovana_generace = generace

    return mutovana_generace
