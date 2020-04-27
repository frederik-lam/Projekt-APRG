import ruzne_funkci as rf
import bio_procesy as bp


def main():
    [matrix, num_of_cities] = rf.file_read()
    num_of_individuals = 10  # int(input("Zadejte mnozstvi potřebných jedincu v generace: "))
    start_city = 3
    generation = bp.create_generation(num_of_cities, num_of_individuals, start_city)
    iteration_max = 1500  # maximalny pocet iteracii
    actual_iteration = 0
    best_scores = []  # hodnoty najlepsich jedincov pre neskorsie vykreslenie do grafu
    best_individuals = []  # najlepsi jedinci

    while actual_iteration != iteration_max:
        [best_individual, best_score] = rf.quality(generation, matrix)
        best_scores.append(best_score)
        best_individuals.append(best_individual)
        crossed_generation = bp.crossingover(generation, best_individual)
        mutated_generation = bp.mutation(crossed_generation)
        generation = mutated_generation.copy()
        actual_iteration += 1
    print(best_individuals)
    print(best_scores)
    rf.quality_plot(best_scores)


if __name__ == "__main__":
    main()
