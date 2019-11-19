class Obleceni:
    def __init__(self, pocet:int, velikost, barva:str, znacka:str):
        self.pocet = pocet
        self.velikost = velikost
        self.barva = barva
        self.znacka = znacka

    def naskladnit(self, cislo):
        self.pocet += cislo

    def prodat(self, cislo):
        self.pocet -= cislo

    def __str__(self):
        return str(self.velikost) + " " + self.barva + " " + str(self.pocet)


class Tricko(Obleceni):
    def __init__(self, pocet:int, velikost, barva:str, znacka:str, limec, v):
        super().__init__(pocet, velikost, barva, znacka)
        self.limecek = limec
        self.v = v


class Kalhoty(Obleceni):
    def __init__(self, pocet:int, velikost, barva:str, znacka:str, typ, material):
        super().__init__(pocet, velikost, barva, znacka)
        self.typ = typ
        self.material = material


class Boty(Obleceni):
    def __init__(self, pocet:int, velikost, barva:str, znacka:str, zima):
        super().__init__(pocet, velikost, barva, znacka)
        self.zima = zima

    def __str__(self):
        return str(self.velikost) + " " + self.znacka + " " + str(self.pocet)


t1 = Tricko(444, "XXL", "Modrá", "Nike", "Ne", "Ano")
k1 = Kalhoty(666, "L", "Černá", "Adidas", "tepláky", "látka")
b1 = Boty(555, 42, "Zelená", "Adidas", "Ne")
print(t1)
print(k1)
print(b1)
t1.prodat(111)
k1.naskladnit(888)
b1.prodat(8)
print(t1)
print(k1)
print(b1)