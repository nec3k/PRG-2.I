class VyvojarskeStudio:
    def __init__(self, nazev, rok_zalozeni, majitel, seznam_her):
        self.nazev = nazev
        self.rok_zalozeni = rok_zalozeni
        self.majitel = majitel
        self.seznam_her = seznam_her  # S tímto seznamem bych mohl dále pracovat
        self.hry = ""
        for i in seznam_her:
            self.hry = self.hry + i.nazev + ", "
        self.hry = self.hry[:-2]  # Tato proměná je zde jen pro vypsání

    def __str__(self):
        return "Vývojářské studio " + self.nazev + " bylo založeno v roce " + str(self.rok_zalozeni) + ". Majitel je " + self.majitel + ". Studio vydalo tyto hry: " + self.hry

    def zmena_majitele(self, novy_majitel):
        self.majitel = novy_majitel

    def vypis_majitele(self):
        return self.majitel


class Hra:
    def __init__(self, nazev, rok_vydani, rekordni_cas):
        self.nazev = nazev
        self.rok_vydani = rok_vydani
        self.rekordni_cas = rekordni_cas

    def __str__(self):
        return "Hra "+self.nazev + " byla vydána v roce "+str(self.rok_vydani)+" a byla nejrychleji dohrána v čase: " + self.rekordni_cas

    def vypis_rekord(self):
        return self.rekordni_cas

    def novy_rekord(self, novy_rekord):
        if int(self.rekordni_cas[0:2]) > int(novy_rekord[0:2]) or int(self.rekordni_cas[0:2]) == int(novy_rekord[0:2]) and int(self.rekordni_cas[3:5]) > int(novy_rekord[3:5]) or int(self.rekordni_cas[0:2]) == int(novy_rekord[0:2]) and int(self.rekordni_cas[3:5]) == int(novy_rekord[3:5]) and int(self.rekordni_cas[6:]) > int(novy_rekord[6:]):
            self.rekordni_cas = novy_rekord
            return "Rekord byl úspněšně změněn"
        else:
            return "Zadaný čas je pomalejší ..."


minecraft = Hra("Minecraft", 2007, "00:48:12")
gtasa = Hra("GTA San Andreas", 2004, "12:04:22")
print(minecraft)
x = minecraft.novy_rekord("01:07:56")
y = minecraft.novy_rekord("00:34:52")
z = gtasa.novy_rekord("11:54:00")
print(x)
print(y)
print(z)
print(minecraft.vypis_rekord())
print(gtasa)
mojang = VyvojarskeStudio("Mojang", 2004, "William Notch", [minecraft, gtasa])
print(mojang)
mojang.zmena_majitele("Karel Vomáčka")
print(mojang.vypis_majitele())

#hh:mm:ss
#01234567
