class Kniha:
    def __init__(self, nazev, vazba, pocet_stran, ISBN, rok_vydani, popis, zanr, cena):
        self.nazev = nazev
        self.vazba = vazba
        self.pocet_stran = pocet_stran
        self.ISBN = ISBN
        self.rok_vydani = rok_vydani
        self.popis = popis
        self.zanr = zanr
        self.cena = cena


class Autor:
    def __init__(self, jmeno, prijmeni, vek, seznam_knih):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.seznam_knih = seznam_knih

    def __str__(self):
        x = ""
        for i in self.seznam_knih:
            x = x + i.nazev + ", "
        return self.jmeno + " " + self.prijmeni + ", " + str(self.vek) + " let. Seznam knih: " + x[0:-2]

    def pridatknihu(self, novakniha):
        self.seznam_knih.append(novakniha)

    def nejstarsi_kniha(self):
        x = self.seznam_knih[0]
        for i in self.seznam_knih:
            if i.rok_vydani < x.rok_vydani:
                x = i
        return "Nejstarší kniha od autora " + self.jmeno + " " + self.prijmeni + " je: " + x.nazev

    def vsechny_ISBN(self):
        x = ""
        for i in self.seznam_knih:
            x = x + str(i.ISBN) + ", "
        return "ISBN knih od autora " + self.jmeno + " " + self.prijmeni + " jsou: "+x[0:-2]

    def soucet_stranek(self):
        x = 0
        for i in self.seznam_knih:
            x += i.pocet_stran
        return "Součet stránek všech knih od autora " + self.jmeno + " " + self.prijmeni+" je: " + str(x)

    def zanry(self):
        x = ""
        for i in self.seznam_knih:
            if i.zanr not in x:
                x = x + i.zanr + ", "
        return self.jmeno + " " + self.prijmeni+" napsal knihy v těchto žánrech: " + x[0:-2]


kniha1 = Kniha("Babička", "Pevná", 420, 888777999, 2012, "Velice zajímavá kniha o Babičkce", "Tragédie", 400)
kniha2 = Kniha("Batman", "Pevná", 333, 888777998, 1958, "Kniha o Dědečkovi", "Tragédie", 220)
kniha3 = Kniha("Malý princ", "Měkká", 9, 888777997, 1988, "Příběh Malého prince", "Komedie", 300)
nemcova = Autor("Karel", "Vomáčka", 41, [kniha1, kniha2])
Autor.pridatknihu(nemcova, kniha3)
print(nemcova)
print(nemcova.nejstarsi_kniha())
print(nemcova.vsechny_ISBN())
print(nemcova.soucet_stranek())
print(nemcova.zanry())
