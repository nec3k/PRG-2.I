class Vojak:
    def __init__(self, id:int, tym, max_vit:int, akt_vit:int, max_dmg:int):
        self.id = id
        self.tym = tym
        self.max_vit = max_vit
        self.akt_vit = akt_vit
        self.max_dmg = max_dmg
        self.pocet_zasahu = 0

    def zasah(self, hodnota:int):
        if hodnota > 0:
            self.akt_vit -= hodnota

    def pal(self):
        from random import randint
        return randint(0, self.max_dmg+1)


class Tym:
    def __init__(self, nazev:str, barva:str, kredit:int, seznam:list):
        self.nazev = nazev
        self.barva = barva
        self.kredit = kredit
        self.seznam = seznam

    def pridat_vojaka(self, novy_vojak:Vojak):
        self.seznam.append(novy_vojak)
        self.kredit -= 5

    def update(self):
        for i in self.seznam:
            if i.akt_vit < 1:
                self.seznam.remove(i)


tym1 = Tym("Tým číslo 1", "Modrá", 100, list())
tym2 = Tym("Tým číslo 2", "Zelená", 100, list())
v1 = Vojak(0, tym1, 15, 15, 10)
v2 = Vojak(1, tym1, 15, 15, 10)
v3 = Vojak(2, tym2, 15, 15, 10)
v4 = Vojak(3, tym1, 15, 15, 10)
print(tym1.kredit)
tym1.pridat_vojaka(v1)
tym1.pridat_vojaka(v2)
tym2.pridat_vojaka(v3)
tym1.pridat_vojaka(v4)
print(tym1.kredit)
for i in range(10):
    x = v1.pal()
    print("Poškození: " + str(x))
    v3.zasah(x)

print("----")
print(v3.akt_vit)
print(tym2.seznam)
tym2.update()
print(tym2.seznam)
