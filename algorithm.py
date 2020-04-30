import ruzne_funkci as rf
import bio_procesy as bp


def main():
    nazev = str(input("Napiste nazev souboru bez uvazovok(priklad: data.csv ): "))
    [matrix, num_of_cities] = rf.file_read(nazev)
    num_of_individuals =  int(input("Zadejte mnozstvi potřebných jedincu v generace (priklad: 60 ): "))
    start_city = int(input("Zadejte pocatecni město (priklad: 5 ): "))
    generation = bp.create_generation(num_of_cities, num_of_individuals, start_city)
    iteration_max = int(input("Zadejte maximalni pocet iteraci(priklad: 500 ): "))
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
    #print("Seznam nejlepsich jedincu v kazde generace: ",best_individuals)
    #print("Seznam nejlepsich score v kazde generace",best_scores)
    print("Nejlepsi zjisteny jedinec: ", best_individual)
    print("A jeho skore: ", best_score)
    rf.quality_plot(best_scores)


if __name__ == "__main__":
    main()
