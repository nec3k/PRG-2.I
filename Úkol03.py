from random import randint


def generovani_a_hledani(seznam, limit):
    if len(seznam) <= limit:
        seznam.append(randint(0,1000))
        generovani_a_hledani(seznam, limit)
    else:
        print(seznam)
        try:
            cislo = int(input("Zadejte hledané číslo:"))
            x = seznam.index(cislo) + 1
            print("Číslo je na pozici", x)
        except ValueError:
            print("Číslo v seznamu není")


generovani_a_hledani(list(), 20)


