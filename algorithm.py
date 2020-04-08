import ruzne_funkci as rf


[matice, poc_mest] = rf.file_read()
mnozstvi_jedincu = 6#int(input("Zadejte mnozstvi potřebných jedincu v generace: "))
start_city = 1#int(input("Zadejte cislo zacatku cesty: "))

generace = rf.create_generation(poc_mest, mnozstvi_jedincu,start_city) # priklad vysledku = [[1, 2, 3, 6, 5, 4], [1, 6, 2, 4, 3, 5]]...
print(generace)
kvality = rf.quality(generace, matice)
print(kvality)
probabilities = rf.qual_to_prob(kvality)
print(probabilities)
zselektovana_generace = rf.selection(probabilities,generace)
print(zselektovana_generace)