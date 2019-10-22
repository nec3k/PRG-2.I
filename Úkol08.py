class Auto:
    def __init__(self, SPZ, VIN, STK_do_data, znacka_auta, typ_auta, barva, typ_karoserie, motor, LP, PP, LZ, PZ):
        self.SPZ = SPZ
        self.VIN = VIN
        self.STK_do_data = STK_do_data
        self.znacka_auta = znacka_auta
        self.typ_auta = typ_auta
        self.barva = barva
        self.typ_karoserie = typ_karoserie
        self.motor = motor
        self.LP = LP
        self.PP = PP
        self.LZ = LZ
        self.PZ = PZ

    def __str__(self):
        return "Auto s SPZ: "+ self.SPZ+ ", VIN: "+ self.VIN + ", STK do data: " + self.STK_do_data + ", značka auta: " + self.znacka_auta + ", typ auta: " + self.typ_auta + ", barva auta: " + self.barva + ", typ karoserie: "+ self.typ_karoserie

    def vypis_info(self):
        return self.znacka_auta, self.typ_auta, self.SPZ

    def prodlouzit_STK(self, nove_datum):
        self.STK_do_data = nove_datum

    def kontrola_tlaku_pneu(self):
        return "Levé přední kolo"+self.LP.kontrola_tlaku(), "Pravé přední kolo"+self.PP.kontrola_tlaku(), "Levé zadní kolo"+self.LZ.kontrola_tlaku(), "Pravé zadní  kolo"+self.PZ.kontrola_tlaku()


class Motor:
    def __init__(self, typ, obsah, palivo):
        self.typ = typ
        self.obsah = obsah
        self.palivo = palivo

    def __str__(self):
        return "Motor: "+ self.typ + ", s obsahem: " + self.obsah + ", na palivo: " + self.palivo


class Kolo:
    def __init__(self, aktualni_tlak, maximalni_tlak, vyrobce_pneumatiky,typ_pneumatiky):
        self.aktualni_tlak = aktualni_tlak
        self.maximalni_tlak = maximalni_tlak
        self.vyrobce_pneumatiky = vyrobce_pneumatiky
        self.typ_pneumatiky = typ_pneumatiky

    def __str__(self):
        return "Aktuální tlak pneumatiky: " + self.aktualni_tlak + ", maximální tlak: " + self.maximalni_tlak + ", výrobce: " + self.vyrobce_pneumatiky + ", typ:" + self.typ_pneumatiky

    def kontrola_tlaku(self):
        if self.aktualni_tlak<=self.maximalni_tlak:
            return "je v pořádku."
        else:
            return "má moc vysoký tlak."


motor1= Motor("HTP", 1.2, "Benzín")
kolo1 = Kolo(4.6, 3, "Aab", "Letní")
kolo2 = Kolo(2.6, 3, "Aab", "Letní")
kolo3 = Kolo(2.6, 3, "Aab", "Letní")
kolo4 = Kolo(2.6, 3, "Aab", "Letní")
auto1 = Auto("0134-A8", "12456ZZA", "2.9.2020", "Škoda", "Fabia", "Červená", "Kombi", motor1, kolo1, kolo2, kolo3, kolo4)
print(auto1)
info = auto1.vypis_info()
print(info)
auto1.prodlouzit_STK("9. 12. 2034")
print(auto1.STK_do_data)
pneu = auto1.kontrola_tlaku_pneu()
print(pneu)