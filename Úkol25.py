import mysql.connector


def pridat(mydb):
    while True:
        nazev_statu = input("Zadejte název nového státu: ")
        while True:
            try:
                rozloha = int(input("Zadejte rozlohu v KM² nového státu: "))
                break
            except ValueError:
                print("Je potřeba zadat celé číslo !")
        id_kontinent = input("Zadejte id kontinent: ")
        if id_kontinent == "":
            id_kontinent = None
        try:
            mycursor = mydb.cursor()
            sql = ("INSERT INTO `staty` (`nazev`, `kontinent_id`, `rozloha`) VALUES (%s, %s, %s);")
            val = (nazev_statu, id_kontinent, rozloha)
            mycursor.execute(sql, val)
            mydb.commit()
            pokracovat = input("Chcete zadat další stát? (ano x ne): ")
            if pokracovat == "ne":
                break
        except mysql.connector.Error:
            print("Asi jste zadali špatné id kontinentu ...")


try:
    mydb = mysql.connector.connect(
        host="studenti.odbornaskola.cz",
        user="uXXX",
        passwd="heslo",
        database="uXXX",
        port="3306")
    pridat(mydb)
except mysql.connector.Error:
    print("Někde se stala chyba ...")
