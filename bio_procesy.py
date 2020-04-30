import random as rnd


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
    :param probabilities: Pravdepodobnost vyberu
    :param generation: Generace, z ktorej vyberame rodica
    :return selected_breeder: Jedinec, ktory bude mat sancu sa krizit
    """
    selected_parent = []
    prob_of_parent = []
    while not selected_parent:  # cyklus prebieha pokial nie je vybraty 1 rodic
        var = round(rnd.random(), 4)  # nahodna hodnota od 0 do 1, sluzi pre uprednostnenie lepsich jedincov
        picked_individual_indx = rnd.randint(0, len(generation)-1)  # nahodne vybranie jedinca z generacie
        if probabilities[picked_individual_indx] - var < 0:  # lepsi jedinci maju hodnotu blizsiu 0, preto budu < 0
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


def crossingover(generace, probs, elite):  # [1,2,4,6,3,5]
    """
    Náhodně promíchání části řetezce
    :param generace: Seznam jedincu
    :param probs: Seznam pravděpodobnosti
    :param elite: Najlepší jedinec z predchádzajúcej generácie
    :return: Zkrosingovany jedinec
    """
    new_generation = []
    new_generation.append(elite)
    gen_len = len(generace)

    while len(new_generation) != gen_len:
        help_gen = generace.copy()  # vytvorenie pomocnej generacie
        help_prob = probs.copy()  # vytvorenie pocnych pravdepodobnosti
        [parent1, prob_parent1] = selection(help_gen, help_prob)  # vybratie rodicov, ktory budu vstupovat do krizenia
        help_gen.remove(parent1)
        help_prob.remove(prob_parent1)  # osetrenie aby nebol 2-krat vybraty ten isty rodic
        [parent2, pprob_parent2] = selection(help_gen, help_prob)

        miesto_krizenia = rnd.randint(int(len(parent1) / 3), int(2 * len(parent1) / 3))
        # vybratie nahodneho miesta krizenia, usudil som ze najlepsie bude ak to bude niekde medzi 1/3 a 2/3 dlzky

        # Rozhodnutie ci bude do novej generacie pridany 1. alebo 2.potomok (lisia sa poradim zaciatku a konca)
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
        [index_1, index_2] = rnd.sample(range(1,delka_jed), 2)  # nahodny vyber 2 prvkov, vynechanie startovacieho mesta
        jedinec[index_1], jedinec[index_2] = jedinec[index_2], jedinec[index_1]  # prehodenie danych prvkov
        generace.insert(i, jedinec)  # vratenie mutovaneho jedinca na povodnu poziciu
    mutovana_generace = generace

    return mutovana_generace
