Seznam = list()
Cislo = int(input("Zadjete číslo:"))


def funkce(seznam, cislo):
    if cislo > -1:
        seznam.append(list(range(0, cislo+1)))
        funkce(seznam, cislo-1)
    else:
        print(seznam)


funkce(Seznam, Cislo)
