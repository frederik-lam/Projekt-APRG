import ruzne_funkci as rf


#[matice, M] = rf.nacteni_souboru(input("Bez uvazovok napiste nazev souboru: "))
[matice, M] = rf.nacteni_souboru("data_vzdalenosti.csv")
mnozstvi_jedincu = 4#int(input("Zadejte mnozstvi potřebných jedincu v generace: "))
start_city = 1#int(input("Zadejte cislo zacatku cesty: "))

generace = rf.create_generation(M, mnozstvi_jedincu,start_city) #[[4, 2, 3, 6, 5, 1], [4, 6, 2, 1, 3, 5], [4, 1, 2, 6, 5, 3], [4, 3, 1, 2, 6, 5]]
kvality = rf.urceni_kvality(generace, matice)

print(kvality)
print(generace)
# new_jed = rf.crossingover([1,2,5,4,3]) #testovani fungovani funkce krizeni
# print(new_jed)
# new_jed = rf.mutation([1,2,5,4,3]) #testovani fungovani funkce mutace
# print(new_jed)



def main():


if __name__ == "__main__":
    main()