from vytvoreni_generace import create_generation

#
#tady my prý zpracujeme tabulku dat MxM, a zjistujeme mnozstvi mest M a vzdalenosti mezi nimi
#

M = 8 #množstvi měst (napriklad)
mnozstvi_jedincu = int(input("Zadejte mnozstvi potřebných jedincu v generace: "))

cisla = list()
for i in range(1, M + 1):
    cisla.append(i)
#var. cisla je seznam cisel jdoucich od 1 do M kterou budeme vyuzivat



def main():

    create_generation(cisla, mnozstvi_jedincu)

if __name__ == "__main__":
    main()