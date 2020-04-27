import mysql.connector

#SELECT `eshop_produkt`.`id`, `eshop_karegorie`.`nazev` FROM `eshop_produkt` JOIN eshop_karegorie ON eshop_karegorie.id = eshop_produkt.kategorie WHERE aktivni=1 AND eshop_karegorie.nazev = "mobily"
def ziskat_data_z_db(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT `eshop_produkt`.`id` FROM `eshop_produkt`")
    myresultt = mycursor.fetchall()
    celkem = len(myresultt)
    mycursor.execute("SELECT `eshop_karegorie`.`id` FROM `eshop_karegorie`")
    myresult = mycursor.fetchall()
    id_kategorii = list()
    pocet_produktu_bez_kategorie=0
    for i in myresult:
        id_kategorii.append(i[0])
    for i in myresultt:
        i=i[0]
        if i not in id_kategorii:
            pocet_produktu_bez_kategorie+=1
    mycursor.execute("SELECT `eshop_karegorie`.`nazev` FROM `eshop_karegorie` WHERE aktivni = 1")
    aktivni_kategorie = mycursor.fetchall()
    seznam = list()
    for i in aktivni_kategorie:
        mycursor.execute("SELECT `eshop_produkt`.`id` FROM `eshop_produkt` JOIN `eshop_karegorie` ON `eshop_karegorie`.`id` = `eshop_produkt`.`kategorie` WHERE eshop_karegorie.nazev = '"+i[0]+"'")
        myresult = mycursor.fetchall()
        seznam.append((i, len(myresult)))
    return str(celkem), seznam, pocet_produktu_bez_kategorie


mydb = mysql.connector.connect(
        host="studenti.odbornaskola.cz",
        user="uXXX",
        passwd="heslo",
        database="uXXX",
        port="3306")
print("V databázi je celkem "+ziskat_data_z_db(mydb)[0]+" produktů.")
nevim = ziskat_data_z_db(mydb)[1]
for i in nevim:
    print("V kategorii "+i[0][0]+" je "+str(i[1])+" produktů.")
print("Počet produktů bez kategorie: "+str(ziskat_data_z_db(mydb)[2]))
