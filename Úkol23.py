import mysql.connector


def vypis(mydb, kontinent):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT 2_21_U25_stat.nazev FROM `2_21_U25_stat` JOIN 2_21_U25_kontinent ON 2_21_U25_stat.kontinent_id = 2_21_U25_kontinent.id WHERE 2_21_U25_kontinent.nazev = \""+kontinent+"\"")
    myresult = mycursor.fetchall()
    vysledek = ""
    if myresult:
        for i in myresult:
            vysledek += i[0]+", "
        print("Na kontinentu " + kontinent + "leží tyto státy: " + vysledek[:-2])
    else:
        print("Kontinent není v databázi nebo na něm neleží žádný stát ...")


nazev_kontinentu = input("Zadejte název kontinentu: ")
try:
    mydb = mysql.connector.connect(
        host="studenti.odbornaskola.cz",
        user="uXXX",
        passwd="heslo",
        database="uXXX",
        port="3306")
    vypis(mydb, nazev_kontinentu)
except mysql.connector.Error:
    print("Připojení do BD se nezdařilo")
