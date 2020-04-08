import ruzne_funkci as rf


[matice, poc_mest] = rf.file_read()
mnozstvi_jedincu = 6#int(input("Zadejte mnozstvi potřebných jedincu v generace: "))
start_city = 1#int(input("Zadejte cislo zacatku cesty: "))

generace = rf.create_generation(poc_mest, mnozstvi_jedincu,start_city) # priklad vysledku = [[1, 2, 3, 6, 5, 4], [1, 6, 2, 4, 3, 5]]...
print("Počateční generace: ", generace)
kvality = rf.quality(generace, matice)
print("Délky cest počateční generace: ", kvality)
probabilities = rf.qual_to_prob(kvality)
print("Pravděpodobnost že projdou do další generace(0 - projdou, 1 - ne): ", probabilities)
[projdene_probabilities, projdena_generace] = rf.selection(generace, probabilities)
print("Generace po selekci: ", projdena_generace)
print("Jejich pravděpodobnosti: ", projdene_probabilities)
zkrossingovana_generace = rf.crossingover(projdena_generace, projdene_probabilities)
print("U nové generace u některých jedinců došlo ke crossoveringů: ", zkrossingovana_generace)
