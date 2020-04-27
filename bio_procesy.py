import random as rnd
# import numpy as np


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


def selection(generation):
    """
    Na zakladě pravděpodobnosti určuje kdo projde do další delka_generace.
    :param generation:
    :return selected_breeder: Jedinec, ktory bude mat sancu sa krizit
    """

    picked_individual_indx = rnd.randint(0, len(generation)-1)  # nahodne vybranie jedinca
    selected_parent = generation[picked_individual_indx]

    return selected_parent


def breed(parent1, parent2, chiasma):
    """
    Vytvorenie potomka z 2 rodicov
    :param parent1: 1.Rodic
    :param parent2: 2.Rodic
    :param chiasma: miesto prekrizenia
    :return offspring:  potomok rodicov
    """
    start = parent1[0:chiasma]  # vynechanie 0 prvku aby sa nezmenilo start city
    tail = [gen for gen in parent2 if gen not in start]
    offspring = start + tail

    return offspring


def crossingover(generace, elite):  # [1,2,4,6,3,5]
    """
    Náhodně promíchání části řetezce
    :param generace: Seznam jedincu
    :param elite: Najlepší jedinec z predchádzajúcej generácie
    :return: Zkrosingovany jedinec
    """
    new_generation = []
    new_generation.append(elite)
    gen_len = len(generace)

    while len(new_generation) != gen_len:
        help_gen = generace.copy()  # vytvorenie pomocnej generacie
        parent1 = selection(help_gen)  # vybratie rodicov, ktory budu vstupovat do krizenia
        help_gen.remove(parent1)
        parent2 = selection(help_gen)

        miesto_krizenia = rnd.randint(int(gen_len / 3), int(2 * gen_len / 3))
        # vybratie nahodneho miesta krizenia, usudil som ze najlepsie bude ak to bude niekde medzi 1/3 a 2/3 dlzky

        # Rozhodnutie ci bude do novej generacie pridany 1. alebo 2.potomok
        a = rnd.random()  # nahodne vybratie cisla
        if a < 0.5:
            offspring1 = breed(parent1, parent2, miesto_krizenia)  # vytvorenie prveho potomka
            new_generation.append(offspring1)
        else:
            offspring2 = breed(parent2, parent1, miesto_krizenia)  # vytvorenei druheho potomka
            new_generation.append(offspring2)

    return new_generation


def mutation(generace):  # [1,2,4,6,3,5]
    """
    Nahodne prohozeni dvou cisel v posloupnosti jedincu.
    Dodat/rozšířit:
    -Vstupem je taky pravděpodobnosti prošle do další delka_generace.
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
