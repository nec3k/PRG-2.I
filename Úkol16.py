class Tvar:
    def __init__(self):
        pass

    def vypocitej_obsah(self):
        pass

    def vypocitej_obvod(self):
        pass


class Kolecko(Tvar):
    def __init__(self, prumer):
        super().__init__()
        self.prumer = prumer
        self.polomer = prumer/2

    def __str__(self):
        return "Průměr je: " + str(self.prumer) + " a poloměr je: " + str(self.polomer)

    def vypocitej_obsah(self):
        from math import pi
        return pi*self.polomer**2

    def vypocitej_obvod(self):
        from math import pi
        return pi*self.prumer


class PravouhlyTrojuhelnik(Tvar):
    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return str(self.a) + ", " + str(self.b) + ", " + str(self.c)

    def vypocitej_obsah(self):
        return (self.a * self.b) / 2

    def vypocitej_obvod(self):
        return self.a + self.b + self.c


class Obdelnik(Tvar):
    def __init__(self, a, b):
        super().__init__()
        self.a = a
        self.b = b

    def __str__(self):
        return str(self.a) + ", " + str(self.b)

    def vypocitej_obsah(self):
        return self.a*self.b

    def vypocitej_obvod(self):
        return 2*(self.a + self.b)


class Ctverec(Obdelnik):
    def __init__(self, a):
        super().__init__(a, a)

    def __str__(self):
        return self.a


k1 = Kolecko(3)
print(k1)
print(k1.vypocitej_obvod())
print(k1.vypocitej_obsah())
pt1 = PravouhlyTrojuhelnik(4, 5, 6)
print(pt1.vypocitej_obvod())
print(pt1.vypocitej_obsah())
o1 = Obdelnik(4, 7)
print(o1.vypocitej_obvod())
print(o1.vypocitej_obsah())
c1 = Ctverec(5)
print(c1.vypocitej_obvod())
print(c1.vypocitej_obsah())
