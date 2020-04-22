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


def selection(generation, probabilities):
    """
    Na zakladě pravděpodobnosti určuje kdo projde do další delka_generace.
    :param probabilities:
    :param generation:
    :return selected_breeder: Jedinec, ktory bude mat sancu sa krizit
    """
    selected_parent = []
    prob_of_parent = []
    while not selected_parent:
        var = round(rnd.random(), 4)  # rand float od 0 do 1
        picked_individual_indx = rnd.randint(0, len(generation)-1)  # nahodne vybranie jedinca
        if probabilities[picked_individual_indx] - var < 0:
            selected_parent = generation[picked_individual_indx]
            prob_of_parent = probabilities[picked_individual_indx]

    return selected_parent, prob_of_parent


def breed(parent1, parent2, chiasma):
    """
    Vytvorenie potomka z 2 rodicov
    :param parent1: 1.Rodic
    :param parent2: 2.Rodic
    :param chiasma: miesto prekrizenia
    :return offspring:  potomok rodicov
    """
    start = parent1[0:chiasma]
    tail = [gen for gen in parent2 if gen not in start]
    offspring = start + tail
    return offspring


def crossingover(generace, probs):  # [1,2,4,6,3,5]
    """
    Náhodně promíchání části řetezce
    :param generace: Seznam jedincu
    :param probs: Seznam pravděpodobnosti
    :return: Zkrosingovany jedinec
    """
    new_generation = []
    gen_len = len(generace)

    while len(new_generation) != gen_len:
        help_gen = generace
        help_prob = probs
        [parent1, prob_parent1] = selection(help_gen, help_prob)  # vybratie rodicov, ktory budu vstupovat do krizenia
        help_gen.remove(parent1)
        help_prob.remove(prob_parent1)  # osetrenie aby nebol 2-krat vybraty ten isty rodic
        [parent2, pprob_parent2] = selection(help_gen, help_prob)

        miesto_krizenia = rnd.randint(int(gen_len / 3), int(2 * gen_len / 3))
        # vybratie nahodneho miesta krizenia, usudil som ze najlepsie bude ak to bude niekde medzi 1/3 a 2/3 dlzky

        offspring1 = breed(parent1, parent2, miesto_krizenia)  # vytvorenie prveho potomka
        offspring2 = breed(parent2, parent1, miesto_krizenia)  # vytvorenei druheho potomka

        # Rozhodnutie ci bude do novej generacie pridany len 1 potomok alebo 2
        if gen_len - len(new_generation) >= 2:
            a = rnd.random()  # nahodne vybratie cisla
            if a < 0.5:  # ak je a < 0.5 tak je vybraty iba jeden potomok, opacne su vybraty obaja
                if a < 0.25:
                    new_generation.append(offspring1)
                else:
                    new_generation.append(offspring2)
            else:
                new_generation.append(offspring1)
                new_generation.append(offspring2)
        else:
            new_generation.append(offspring1)
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
    pocet_mutovanych_jedincov = rnd.randint(0, gen_length)  # nahodny vzber poctu mutovanych jedincov
    indx_mutovanych_jedincov = rnd.sample(range(gen_length), pocet_mutovanych_jedincov)  # nahodny vyber jedincov u
    # ktorych dojde k mutacii
    mutovana_generace = generace
    for i in indx_mutovanych_jedincov:
        jedinec = generace[i]
        mutovana_generace.pop(i)  # odstranenie jedinca y povodnej generacie
        delka_jed = len(jedinec)
        [index_1, index_2] = rnd.sample(range(delka_jed), 2)  # nahodny vyber 2 prvkov
        jedinec[index_1], jedinec[index_2] = jedinec[index_2], jedinec[index_1]  # prehodenie danych prvkov
        mutovana_generace.insert(i, jedinec)

    return mutovana_generace
