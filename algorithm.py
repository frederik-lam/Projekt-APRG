import ruzne_funkci as rf
import bio_procesy as bp


def main():
    [matrix, num_of_cities] = rf.file_read()
    num_of_individuals = int(input("Zadejte množství potřebných jedincu v generaci: "))
    start_city = int(input("Zadajte startovacie mesto: "))
    if start_city not in range(1,num_of_cities+1):
        raise ValueError("Zadajte štartovacie mesto v rozsahu počtu miest!")
    generation = bp.create_generation(num_of_cities, num_of_individuals, start_city)
    iteration_max = int(input("Zadajte počet iterácii: ")) # maximalny pocet iteracii
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
    # print(best_individuals)
    print(best_scores)  # hodnoty najlepsich jedincov v generacii
    rf.quality_plot(best_scores)


if __name__ == "__main__":
    main()
