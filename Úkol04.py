def mocniny(seznam, cislo):
    if len(seznam)==0:
        seznam.append(cislo)
        mocniny(seznam, cislo)
    elif seznam[-1]*cislo<10000:
        seznam.append(seznam[-1]*cislo)
        mocniny(seznam,cislo)
    else:
        print("Mocniny čísla", cislo, "jsou:", seznam)


x = int(input("Zadejte číslo:"))
mocniny(list(), x)
