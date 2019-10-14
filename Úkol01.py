Seznam = list()
Cislo = int(input("Zadjete číslo:"))


def nasobky(seznam, cislo):
    if cislo < 500:
        seznam.append(cislo)
        nasobky(seznam, cislo + seznam[0])
    else:
        print(seznam)


nasobky(Seznam, Cislo)
