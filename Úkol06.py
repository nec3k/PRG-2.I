s = [299, 435, 3, 4, 68, 9, 65, 4, 3, 11, 89, 45, 9, 5, 77, 34, 21, 16, 19, 49, 50, 10, 333, 6]


def razeni(seznam):
    delka = len(seznam)
    for i in range(delka):
        for r in range(delka-i-1):
            if seznam[r] > seznam[r+1]:
                seznam[r+1], seznam[r] = seznam[r], seznam[r+1]


razeni(s)
print("Seřazený seznam je:")
print(s)

#Nebo pomocí s = sorted(s), které v zadání není zmíněné jako zakázané
