import csv
import numpy as np
import matplotlib.pyplot as plt


def file_read(nazev):
    """
    Nacteni csv souboru s daty, overovani spravneho formatu, vytvoreni matice(array)
    :return: Matice hodnoceni delek cest mezi mesty, pocet mest
    """
    formaty = ["csv", "xls", "xlsx"]
    soubor = nazev.split('.')

    if len(soubor) >= 2:
        file_format = soubor[-1].lower()
        if file_format not in formaty:
            raise ValueError("Spatne zadany format souboru")
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

    [m, n] = mat.shape
    for row in range(m):
        for column in range(n):
            if row == column:
                continue
            elif int(mat[row, column]) < 0:
                raise ValueError("Súbor obsahuje zápornú vzdialenosť na: {0} riadku, {1}stĺpci.".format(str(row + 1),
                                                                                                       str(column + 1)))

    return mat, pocet_mest


def quality(generace, mat_hod):
    """
    Určuje kvalitu generace(délku cest)
    :param generace: Seznam s jedinci
    :param mat_hod: Skorovaci matice, zpracovana data.
    :return: Seznam délek cest jednotlivých jedinců, první index v seznamu odpovidá prvnímu v generace
    """
    kvality = []
    for j in generace:
        kval = 0
        for i in range(len(j)-1):
            kval += int(mat_hod[j[i] - 1][j[i + 1] - 1])
        kval += int(mat_hod[j[0] - 1][j[-1] - 1])  # cesta z posledneho mesta do pociatocneho
        kvality.append(kval)
    best_score = min(kvality)  # hodnota kvality najlepsieho jedinca (pre vykreslenie v grafoch)
    best_pos = kvality.index(best_score)  # najdenie indexu najlepsieho jedinca
    best_individual = generace[best_pos]  # najlepsi jedinec z danej generacie

    return kvality, best_individual, best_score


def qual_to_prob(kvality):
    """
    Transformace kvalit(délek cest) do pravděpodobnosti.
    Nejkratší cesta = 0 pravdepodobnost, největší = 1.
    :param kvality: Seznam s delky cest jedincu v generace
    :return: List s pravdepodobnostmi
    """
    arr = np.array(kvality)

    probabilities_arr = arr - min(arr)    # vycitame nejmensi
    if not np.mean(probabilities_arr) == min(probabilities_arr):
        probabilities_arr = np.around(probabilities_arr / max(probabilities_arr), 4)    # pak vydelime nejvetsim

    probabilities_list = np.ndarray.tolist(probabilities_arr)

    return probabilities_list


def quality_plot(best_individuals):
    """
    Vykreslenie postupného zlepšovania kvality najlepších jedincov v generácii
    :param best_individuals: vektor hodnot kvality najlepších jedincov
    :return: vykreslenie grafu
    """
    plt.plot(best_individuals)
    plt.xlabel('Počet iterací [-]')
    plt.ylabel('Kvalita [-]')
    plt.title('Kvalita nejlepšího jedince')
    plt.show()
