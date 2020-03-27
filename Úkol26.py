import mysql.connector


def vypis(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT `2_21_U25_stat`.`id`, `2_21_U25_stat`.`nazev`, `2_21_U25_kontinent`.`nazev` FROM `2_21_U25_stat` LEFT JOIN `2_21_U25_kontinent` ON `2_21_U25_stat`.`kontinent_id`=`2_21_U25_kontinent`.`id`")
    myresult = mycursor.fetchall()
    myresult.sort(key=lambda tup: tup[1])
    if myresult:
        print("id, název, kontinent_id, rozloha:")
        for i in myresult:
            print(i)


def smazat(mydb, id_statu):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT nazev FROM `2_21_U25_stat` WHERE id = "+id_statu)
    myresult = mycursor.fetchone()
    if myresult:
        mycursor.execute("DELETE FROM `2_21_U25_stat` WHERE `2_21_U25_stat`.`id` = "+id_statu)
        potvrzeni = input("Opravdu chcete smazat "+myresult[0]+"? (Ano/Ne): ")
        if potvrzeni.lower() == "ano":
            mydb.commit()
            print("Stát "+myresult[0]+" byl úspěšně smazán!")
    else:
        print("Stát s tímto ID neexistuje ...")


try:
    mydb = mysql.connector.connect(
        host="studenti.odbornaskola.cz",
        user="uXXX",
        passwd="heslo",
        database="uXXX",
        port="3306")
    vypis(mydb)
    stat = input("Zadejte id státu, který chcete smazat:")
    smazat(mydb, stat)
except mysql.connector.Error:
    print("Někde se stala chyba ...")
