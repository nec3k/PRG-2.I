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

    def __str__(self):
        return "Kniha "+self.nazev+", vazba: "+self.vazba+", počet stran: "+ str(self.pocet_stran) + ", ISBN: "+ str(self.ISBN) + ", rok vydání: "+ str(self.rok_vydani)+", popis: "+self.popis+", žánr: "+self.zanr+", cena: "+str(self.cena)+"Kč"


class Autor:
    def __init__(self, jmeno, prijmeni, vek, seznam_knih):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.seznam_knih = seznam_knih
        self.autorovy_knihy = ""
        for i in self.seznam_knih:
            self.autorovy_knihy = self.autorovy_knihy + i.nazev + ", "
        self.autorovy_knihy = self.autorovy_knihy[0:-2]

    def __str__(self):
        return self.jmeno + " " + self.prijmeni + ", " + str(self.vek) + " let. Seznam knih: " + self.autorovy_knihy

    def pridatknihu(self, novakniha):
        self.seznam_knih.append(novakniha)
        self.autorovy_knihy = self.autorovy_knihy + ", " + novakniha.nazev

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


kniha1 = Kniha("Babička", "Pevná", 421, 888777999, 2012, "Velice zajímavá kniha o Babičce", "Tragédie", 400)
kniha2 = Kniha("Batman", "Pevná", 333, 888777998, 1958, "Kniha o Superhrdinovi", "Tragédie", 220)
kniha3 = Kniha("Malý princ", "Měkká", 9, 888777997, 1988, "Příběh Malého prince", "Komedie", 300)
osoba = Autor("Karel", "Vomáčka", 41, [kniha1, kniha2])
Autor.pridatknihu(osoba, kniha3)
print(osoba)
print(osoba.nejstarsi_kniha())
print(osoba.vsechny_ISBN())
print(osoba.soucet_stranek())
print(osoba.zanry())
print(kniha1)
print(osoba.autorovy_knihy)
