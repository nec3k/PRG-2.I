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


class Tablet(Mobil):
    def __init__(self, velikost_displeje, vaha, cena, pocet_sim, typ_sim, sloty_na_sdkartu):
        super().__init__(velikost_displeje, vaha, cena, pocet_sim, typ_sim)
        self. sloty_na_sd = sloty_na_sdkartu


class LCD_Monitor(elektro):
    def __init__(self, velikost_displeje, vaha, cena, dalkove_ovladani):
        super().__init__(velikost_displeje, vaha, cena)
        self.dalkove_ovladani = dalkove_ovladani


mobil1 = Mobil(5.5, 198, 6666, 2, "Nano SIM")
notebook1 = Ntb(15.6, 2.5, 19999, 512, "Ano")
tablet1 = Tablet(8, 321, 4569, 0, "---", 2)
monitor = LCD_Monitor(24, 1.3, 2499, "Ne")
mobil1.zvys_cenu(50)
print(mobil1.cena)