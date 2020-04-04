import random

mnozstvi_jedincu = int(input("Zadejte mnozstvi potřebných jedincu: "))

def vytvoreni_generace(sezn_cisel, mnozstvi_jedincu):
    generace = []
    for i in range(mnozstvi_jedincu):
        generace.append(random.sample(sezn_cisel, len(sezn_cisel)))

    return generace, print(generace)

def main():

    vytvoreni_generace([1,2,3,4,5], mnozstvi_jedincu)

if __name__ == "__main__":
    main()

