import ruzne_funkci as rf
import bio_procesy as bp


def main():

    [matrix, num_of_cities] = rf.file_read()
    num_of_individuals = 6  # int(input("Zadejte mnozstvi potřebných jedincu v generace: "))
    start_city = 3
    generation = bp.create_generation(num_of_cities, num_of_individuals, start_city)
    iteration_max = 100  # maximalny pocet iteracii
    actual_iteration = 0
    best_scores = []  # hodnoty najlepsich jedincov pre neskorsie vykreslenie do grafu
    best_individuals = []  # najlepsi jedinci
    #print("generace prvni: ", generation)

    while actual_iteration <= iteration_max:
        print("1 krok")
        [quality, best_individual, best_score] = rf.quality(generation, matrix)
        print("2 krok")
        best_scores.append(best_score)
        best_individuals.append(best_individual)
        print("3 krok")
        probs = rf.qual_to_prob(quality)
        #print("probs: ", probs)
        print("4 krok")
        print(generation, probs)
        new_generation = bp.selekcia(generation, probs)
        #print("nova generace: ", new_generation)
        #print("nove probs: ", new_probs)
        print("5 krok")
        crossed_generation = bp.crossingover(new_generation)
        #print("zkrosingovany: ", crossed_generation)
        print("6 krok")
        mutated_generation = bp.mutation(crossed_generation)
        #print("zmutovany: ", mutated_generation)
        #print("7 krok")
        generation = mutated_generation.copy()
        actual_iteration += 1


    #print(best_individuals)
    print(best_scores)
    print(min(best_scores))
    rf.quality_plot(best_scores)


if __name__ == "__main__":
    main()
