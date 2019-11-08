class elektro:
    def __init__(self, velikost_displeje, vaha, cena):
        self.velikost_displeje = velikost_displeje
        self.vaha = vaha
        self.cena = cena

    def zvys_cenu(self, procenta):
        self.cena = self.cena * (1+procenta/100)


class Ntb(elektro):
    def __init__(self, velikost_displeje, vaha, cena, velikost_hdd, lan):
        super().__init__(velikost_displeje, vaha, cena)
        self.hdd = velikost_hdd
        self.lan = lan


class Mobil(elektro):
    def __init__(self, velikost_displeje, vaha, cena, pocet_sim, typ_sim):
        super().__init__(velikost_displeje, vaha, cena)
        self.pocet_sim = pocet_sim
        self.typ_sim = typ_sim


mobil1 = Mobil(5.5, 198, 6666, 2, "Nano SIM")
notebook1 = Ntb(15.6, 2.5, 19999, 512, "Ano")
mobil1.zvys_cenu(50)
print(mobil1.cena)
