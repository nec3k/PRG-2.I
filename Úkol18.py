class Figurka:
    def __init__(self, nazev, barva):
        self.nazev = nazev
        self.barva = barva

    def __str__(self):
        return self.nazev + ", " + self.barva

    def mozna_pozice(self, x, y):
        pozice = []

        def kontrola(seznam_pozic):
            for ii in seznam_pozic[:]:
                for rr in ii:
                    if rr not in range(1, 9):
                        seznam_pozic.remove(ii)
                        break
            return seznam_pozic

        def vez(x1, y1):
            seznam_pozic = []
            for ii in range(1, 9):
                seznam_pozic.append([ii, y1])
                seznam_pozic.append([x1, ii])
            return seznam_pozic

        def strelec(x1, y1):
            seznam_pozic = []
            for ii in range(1, 9):
                seznam_pozic.append([x1 + ii, y1 + ii])
                seznam_pozic.append([x1 + ii, y1 - ii])
                seznam_pozic.append([x1 - ii, y1 + ii])
                seznam_pozic.append([x1 - ii, y1 - ii])
            return seznam_pozic

        if self.nazev == "pěšák":
            if self.barva == "bílá":
                y = y+1
                if y < 9:
                    return [[x, y]]
            if self.barva == "černá":
                y = y-1
                if y > 0:
                    return [[x, y]]
        if self.nazev == "jezdec":
            pozice = [[x+2, y+1], [x+2, y-1], [x-2, y+1], [x-2, y-1], [x+1, y+2], [x-1, y+2], [x+1, y-2], [x-1, y-2]]
            pozice = kontrola(pozice)
            return pozice
        if self.nazev == "střelec":
            pozice = strelec(x, y)
            pozice = kontrola(pozice)
            return pozice
        if self.nazev == "věž":
            pozice = vez(x, y)
            return pozice
        if self.nazev == "dáma":
            pozice1 = vez(x, y)
            pozice2 = strelec(x, y)
            pozice2 = kontrola(pozice2)
            pozice = pozice1 + pozice2
            return pozice
        if self.nazev == "král":
            pozice = [[x+1, y+1], [x+1, y], [x+1, y-1], [x, y+1], [x, y], [x, y-1], [x-1, y+1], [x-1, y], [x-1, y-1]]
            pozice = kontrola(pozice)
            return pozice


class Sachovnice:
    def __init__(self):
        def vytvor_sachovnice():
            abc = "hgfedcba"
            sachovnice = []
            for i in range(1, 9):
                temp = []
                for r in range(0, 8):
                    temp.append(abc[r]+str(i))
                sachovnice.append(temp)
            return sachovnice

        self.prazdna_sachovnice = vytvor_sachovnice()
        self.sachovnice = vytvor_sachovnice()

    def zjisti_barvu(self, x, y):
        if 0 < x < 9 and 0 < y < 9:
            if x % 2 == 0:
                if y % 2 == 0:
                    return "Černá"
                else:
                    return "Bílá"
            elif x % 2 == 1:
                if y % 2 == 0:
                    return "Bílá"
                else:
                    return "Černá"
        else:
            return "Zadali jste moc vysoké číslo"

    def umistit_figurku(self, x, y, figurka):
        self.sachovnice[y-1][x-1] = figurka

    def posun_figurku(self, x, y, nove_x, nove_y):
        x -= 1
        y -= 1
        nove_x -= 1
        nove_y -= 1
        try:
            kontrola = self.sachovnice[y][x].nazev
        except AttributeError:
            return "Zde není figurka ..."
        figura = self.sachovnice[y][x]
        self.sachovnice[y][x] = self.prazdna_sachovnice[y][x]
        self.sachovnice[nove_y][nove_x] = figura

    def pocet_figurek(self):
        pocet = 0
        for i in self.sachovnice:
            for r in i:
                try:
                    kontrola = r.nazev
                    pocet += 1
                except AttributeError:
                    pass
        return pocet


def vypsat(sachovnicee):
    for i in sachovnicee:
        print(i)


bp = Figurka("pěšák", "bílá")
cp = Figurka("pěšák", "černá")
bv = Figurka("věž", "bílá")
ck = Figurka("král", "černá")
bs = Figurka("střelec", "bílá")
cd = Figurka("dáma", "černá")
bj = Figurka("jezdec", "bílá")
a = Sachovnice()
vypsat(a.sachovnice)
print(a.zjisti_barvu(1, 1))
a.umistit_figurku(1, 2, bp)
a.umistit_figurku(4, 7, cp)
vypsat(a.sachovnice)
print(a.pocet_figurek())
bp_pos = bp.mozna_pozice(1, 2)
print(bp_pos)
a.posun_figurku(1, 2, bp_pos[0][0], bp_pos[0][1])
cp_pos = cp.mozna_pozice(4, 7)
a.posun_figurku(4, 7, cp_pos[0][0], cp_pos[0][1])
vypsat(a.sachovnice)
print(bv.mozna_pozice(4, 2))
print(ck.mozna_pozice(8, 3))
print(bs.mozna_pozice(4, 7))
print(cd.mozna_pozice(3, 5))
print(bj.mozna_pozice(2, 1))
