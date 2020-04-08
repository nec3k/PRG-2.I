import mysql.connector
from time import sleep


def pridat_kontinent(mydb, nazev_kontinentu):
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO `U25_kontinent` (`id`, `nazev`) VALUES (NULL, '"+nazev_kontinentu+"')")
    mydb.commit()
    print("Kontinent byl úspěšně přidán do databáze! ")


def pridat_stat(mydb, nazev_statu, rozloha, id_kontinent):
    mycursor = mydb.cursor()
    sql = ("INSERT INTO `U25_stat` (`nazev`, `kontinent_id`, `rozloha`) VALUES (%s, %s, %s);")
    val = (nazev_statu, id_kontinent, rozloha)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Stát byl úspěšně přidán do databáze! ")


def seradit_a_vypsat(myresult):
    myresult.sort(key=lambda tup: tup[1])
    if myresult:
        print("id, název, kontinent, rozloha:")
        for i in myresult:
            print(i)


def ziskat_data_z_db(mydb, volba):
    mycursor = mydb.cursor()
    if volba == 1:
        mycursor.execute("SELECT `U25_stat`.`id`, `U25_stat`.`nazev`, `U25_kontinent`.`nazev` FROM `U25_stat` LEFT JOIN `U25_kontinent` ON `U25_stat`.`kontinent_id`=`U25_kontinent`.`id`")
    if volba == 2:
        mycursor.execute("SELECT id, nazev FROM `U25_kontinent` ")
    if volba == "idk":
        mycursor.execute("SELECT id FROM `U25_kontinent` ")
        id = list()
        for i in mycursor.fetchall():
            for j in i:
                id.append(int(j))
        print(id)
        return id
    myresult = mycursor.fetchall()
    return myresult


def input_pro_pridat_stat(mydb):
    id_vsech_kontinentu = ziskat_data_z_db(mydb, "idk")
    nazev_statu = input("Zadejte název nového státu: ")
    while True:
        try:
            rozloha = int(input("Zadejte rozlohu v KM² nového státu: "))
            break
        except ValueError:
            print("Je potřeba zadat celé číslo !")
    while True:
        try:
            id_kontinent = input("Zadejte id kontinentu: ")
            if id_kontinent == "":
                id_kontinent = None
                break
            if int(id_kontinent) in id_vsech_kontinentu:
                id_kontinent = int(id_kontinent)
                break
            else:
                raise ValueError
        except ValueError:
            print("Kontinent s tímto ID neexistuje")
    return nazev_statu, rozloha, id_kontinent


def menu():
    print("""
    (1) Vypsat seznam států
    (2) Vypsat seznam kontinentů
    (3) Vložit nový stát
    (4) Vložit nový kontinent
    (5) Smazat stát podle ID
    (6) Smazat kontinent podle ID
    (7) Konec aplikace\n""")
    while True:
        try:
            akce = int(input("Co chceš udělat: "))
            if akce not in range(1, 8):
                raise ValueError
            return akce
        except ValueError:
            print("Zadejte číslo od 1 do 7")


def smazat_stat(mydb, id_statu):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT nazev FROM `U25_stat` WHERE id = "+id_statu)
    myresult = mycursor.fetchone()
    if myresult:
        mycursor.execute("DELETE FROM `U25_stat` WHERE `U25_stat`.`id` = "+id_statu)
        potvrzeni = input("Opravdu chcete smazat "+myresult[0]+"? (Ano/Ne): ")
        if potvrzeni.lower() == "ano":
            mydb.commit()
            print("Stát "+myresult[0]+" byl úspěšně smazán!")
    else:
        print("Stát s tímto ID neexistuje ...")


def smazat_kontinent(mydb, id_kontinentu):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT nazev FROM `U25_kontinent` WHERE id = "+id_kontinentu)
    myresult = mycursor.fetchone()
    if myresult:
        mycursor.execute("DELETE FROM `U25_kontinent` WHERE `U25_kontinent`.`id` = "+id_kontinentu)
        potvrzeni = input("Opravdu chcete smazat "+myresult[0]+"? (Ano/Ne): ")
        if potvrzeni.lower() == "ano":
            mydb.commit()
            print(myresult[0]+" byl úspěšně smazán!")
    else:
        print("Kontinent s tímto ID neexistuje ...")


def spustit_program(mydb):
    volba = 0
    while volba !=7:
        volba = menu()
        if volba in range(1, 3):
            seradit_a_vypsat(ziskat_data_z_db(mydb, volba))
            sleep(2)
        if volba == 3:
            nazev, rozloha, id_kontinentu = input_pro_pridat_stat(mydb)
            pridat_stat(mydb, nazev, rozloha, id_kontinentu)
        if volba == 4:
            nazev_kontinentu = input("Zadejte název nového kontinentu: ")
            pridat_kontinent(mydb, nazev_kontinentu)
        try:
            if volba == 5:
                id = input("Zadejte ID státu, který chcete smazat: ")
                smazat_stat(mydb, id)
            if volba == 6:
                id = input("Zadejte ID kontinentu, který chcete smazat: ")
                smazat_kontinent(mydb, id)
        except mysql.connector.ProgrammingError:
            print("Zadali jste špatné ID! ")
        except mysql.connector.IntegrityError:
            print("Tento kontinent nelze smazat, na něm leží nějaké státy ...")
        sleep(0.5)


mydb = mysql.connector.connect(
        host="studenti.odbornaskola.cz",
        user="uXXX",
        passwd="heslo",
        database="uXXX",
        port="3306")
spustit_program(mydb)
