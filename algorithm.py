import ruzne_funkci as rf
import bio_procesy as bp

# [matice, poc_mest] = rf.file_read()
# mnozstvi_jedincu = 6  # int(input("Zadejte mnozstvi potřebných jedincu v generace: "))
# pocatecne_mesto = 1  # int(input("Zadejte cislo zacatku cesty: "))
#
# generace = bp.create_generation(poc_mest, mnozstvi_jedincu,
#                                 pocatecne_mesto)  # priklad vysledku = [[1, 2, 3, 6, 5, 4], [1, 6, 2, 4, 3, 5]]...
# print("Počateční generace: ", generace)
#
# [kvality, najlepsi_jedinec] = rf.quality(generace, matice)
# print("Délky cest počatečních generaci: ", kvality)
#
# probabilities = rf.qual_to_prob(kvality)
# print("Pravděpodobnost, že projdou do další generace(0 - ano, 1 - ne): ", probabilities)
#
# zkrossingovana_generace = bp.crossingover(generace, probabilities)
# print("V nové generace, u některých jedinců došlo ke crossoveringů: ", zkrossingovana_generace)
#
# mutovana_generace = bp.mutation(zkrossingovana_generace)
# print("Genracia po mutacii: ", mutovana_generace)


def main():
    [matrix, num_of_cities] = rf.file_read()
    num_of_individuals = 6  # int(input("Zadejte mnozstvi potřebných jedincu v generace: "))
    start_city = 1
    generation = bp.create_generation(num_of_cities, num_of_individuals, start_city)
    iteration_max = 10  # maximalny pocet iteracii
    actual_iteration = 0
    best_scores = []  # hodnoty najlepsich jedincov pre neskorsie vykreslenie do grafu
    best_individuals = []  # najlepsi jedinci

    while actual_iteration != iteration_max:
        [quality, best_individual, best_score] = rf.quality(generation, matrix)
        best_scores.append(best_score)
        best_individuals.append(best_individual)
        probs = rf.qual_to_prob(quality)
        crossed_generation = bp.crossingover(generation, probs, best_individual)
        mutated_generation = bp.mutation(crossed_generation)
        generation = mutated_generation.copy()
        actual_iteration += 1
    print(best_individuals)
    print(best_scores)
    rf.quality_plot(best_scores)

main()
