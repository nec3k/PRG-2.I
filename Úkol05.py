from random import randint
Seznam = []
for i in range(20):
    Seznam.append(randint(0,1000))
print(Seznam)


def min(seznam):
    min = seznam[0]
    for i in seznam:
        if i < min:
            min = i
    print("Nejmenší číslo v seznamu je", min, "a je na pozici", seznam.index(min)+1)


def max(seznam):
    maximal = seznam[0]

    def maximum(sseznam, cislo, poradi):
        if poradi<len(seznam):
            if cislo<sseznam[poradi]:
                maximum(sseznam, seznam[poradi], poradi+1)
            else:
                maximum(sseznam, cislo, poradi+1)
        else:
            print("Největší číslo v seznamu je", cislo, "a je na pozici", seznam.index(cislo)+1)
    maximum(seznam, maximal, 0)


min(Seznam)
max(Seznam)