import ruzne_funkci as rf
import bio_procesy as bp

[matice, poc_mest] = rf.file_read()
mnozstvi_jedincu = 6#int(input("Zadejte mnozstvi potřebných jedincu v generace: "))
start_city = 1#int(input("Zadejte cislo zacatku cesty: "))

generace = bp.create_generation(poc_mest, mnozstvi_jedincu,start_city) # priklad vysledku = [[1, 2, 3, 6, 5, 4], [1, 6, 2, 4, 3, 5]]...
print("Počateční generace: ", generace)

najlepsi_jedinci = []  # hodnoty najlepsich jedincov pre neskorsie vykreslenie do grafu
[kvality, najlepsi_jedinec] = rf.quality(generace, matice)
najlepsi_jedinci.append(najlepsi_jedinec)
print("Délky cest počatečních generaci: ", kvality)

probabilities = rf.qual_to_prob(kvality)
print("Pravděpodobnost, že projdou do další generace(0 - ano, 1 - ne): ", probabilities)

# [projdena_generace, projdene_probabilities] = bp.selection(generace, probabilities)
# print("Generace po selekci: ", projdena_generace)
# print("Jejich pravděpodobnosti: ", projdene_probabilities)

zkrossingovana_generace = bp.crossingover(generace, probabilities)
#print("S temíto pravděpodobnosti dojde ke crossoveringů: ", probs_arr)
print("V nové generace, u některých jedinců došlo ke crossoveringů: ", zkrossingovana_generace)

mutovana_generace = bp.mutation(zkrossingovana_generace)
print("Genracia po mutacii: ", mutovana_generace)
