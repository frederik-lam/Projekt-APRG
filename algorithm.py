from ruzne_funkci import create_generation
from ruzne_funkci import crossingover
from ruzne_funkci import mutation

#
#tady my prý zpracujeme tabulku dat MxM, a zjistujeme mnozstvi mest M a vzdalenosti mezi nimi
#

M = 5 #množstvi měst (napriklad)

mnozstvi_jedincu = int(input("Zadejte mnozstvi potřebných jedincu v generace: "))
start_city = int(input("Zadejte cislo zacatku cesty: "))

cisla = list() #cisla je seznam cisel jdoucich od 1 do M, ktery budeme vyuzivat ve vytvoreni generace a jedincu tam nachazeicich
for i in range(1, M + 1):
    cisla.append(i)

def main():

    create_generation(cisla, mnozstvi_jedincu, start_city)
    #crossingover([1,4,2,3,5])
    #mutation([1,2,3,4,5])

if __name__ == "__main__":
    main()