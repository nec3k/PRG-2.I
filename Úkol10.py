class Email:
    def __init__(self, predmet, obsah, datum, pozvrzeno, odesilatel, prijemce):
        self.predmet = predmet
        self.obsah = obsah
        self.datum = datum
        self.potvrzeno = pozvrzeno
        self.odesilatel = odesilatel
        self.prijemce = prijemce

    def __str__(self):
        return "Email s předmětem "+self.predmet+" obsahuje: " + self.obsah + "s datumem " + self.datum + ", potvrzení: "+self.potvrzeno

    def odeslat_email(self):
        pass

    def info_odesilatele(self):
        return self.odesilatel.__str__()

    def info_prijemce(self):
        return self.prijemce.__str__()

class Osoba:
    def __init__(self, jmeno, prijmni, email, email_server):
        self.jmeno = jmeno
        self.prijmeni = prijmni
        self.email = email
        self.email_server = email_server

    def celejmeno(self):
        return self.jmeno + " " + self.prijmeni

    def __str__(self):
        return self.celejmeno() + " má email " + self.email + " a používá tento emailový server: " + self.email_server


os1 = Osoba("Karel", "Vomáčka", "karel@odbornaskola.cz", "postak.odbornaskola.cz")
os2 = Osoba("Prokop", "Buben", "prokop@odbornaskola.cz", "postak.neodbornaskola.cz")
zprava1 = Email("Pozvánka", "Nějaký obsah emailu ... ", "1. 2. 2019", "Ano", os1, os2)
print(os1)
print(os2)
print(zprava1)
print(zprava1.info_prijemce())
print(zprava1.info_odesilatele())
