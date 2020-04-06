from random import sample
from random import randint

def create_generation(sezn_cisel, mnozstvi_jedincu, start_city):
    """
    vytvari seznam obsahujici jedincy,predstavujici sebou jednotlive seznamy s nahodne promichanymi cisly, se stejnym zacatkem.
    :param sezn_cisel: seznam cisel od 1 do M(mnozstvi mest)
    :param mnozstvi_jedincu: zadejme kolik jedincu budeme chtit v generace, ktera pak se bude menit ale mnozstvi jedincu ne.
    :return:
    """
    generace = []
    for i in range(mnozstvi_jedincu):
        generace.append(sample(sezn_cisel, len(sezn_cisel)))
        generace[i].remove(start_city)
        generace[i].insert(0, start_city)

    return generace, print(generace)

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

    return new_jedinec, print(new_jedinec)

def mutation(jedinec):
    """
    nahodne prohozeni dvou cisel v posloupnosti
    :param jedinec: posloupnost cisel
    :return:
    """
    index_1 = randint(1, len(jedinec) - 1)
    index_2 = randint(1, len(jedinec) - 1)

    jedinec[index_1], jedinec[index_2] = jedinec[index_2], jedinec[index_1]

    return jedinec, print(jedinec)
