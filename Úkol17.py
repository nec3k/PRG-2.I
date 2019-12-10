class Film:
    def __init__(self, nazev:str, delka:int, rok:int):
        self.nazev = nazev
        self.delka = delka
        self.rok = rok

    def __str__(self):
        return self.nazev + ", " + str(self.delka) + "min, " + str(self.rok)


def zapsat(nazev_souboru, seznam_filmu):
    soubor = open(nazev_souboru, "w")
    for i in seznam_filmu:
        soubor.write(i.nazev+";"+str(i.delka)+";"+str(i.rok)+"\n")


def nacist(nazev_souboru):
    try:
        soubor = open(nazev_souboru, "r")
    except FileNotFoundError:
        return []
    seznam_filmu = []
    for lines in soubor:
        lines = lines[:-1]
        x, y, z = lines.split(";")
        film = Film(x, y, z)
        seznam_filmu.append(film)
    return seznam_filmu


seznam_filmu = nacist("filmy.txt")
while True:
    nazev = str(input("Zadejte název filmu: "))
    if nazev.lower() == "konec" or nazev == "":
        break
    while True:
        try:
            delka = int(input("Zadejte délku filmu v minutách: "))
        except ValueError:
            print("Nezadali jste celé číslo ...")
            continue
        break
    while True:
        try:
            rok = int(input("Zadejte rok vydání filmu: "))
        except ValueError:
            print("Nezadali jste celé číslo ...")
            continue
        break
    film = Film(nazev, delka, rok)
    seznam_filmu.append(film)
    print("Film úspěšně přidán. ")
zapsat("filmy.txt", seznam_filmu)
