import mysql.connector
from tkinter import *


def nove_okno(nadpis: str):
    window = Tk()
    window.focus_force()
    window.title(nadpis)
    window.option_add("*font", "arial 14")
    return window


def seznam_a():
    global mydb
    window = nove_okno("Knihovna - seznam autorů")
    rada = 0
    polozka = 0
    lbl_id = Label(window, text="ID", borderwidth=1, relief="solid")
    lbl_id.grid(row=0, column=0, sticky="nsew")
    lbl_jmeno = Label(window, text="Jméno", borderwidth=1, relief="solid")
    lbl_jmeno.grid(row=0, column=1, sticky="nsew")
    lbl_prijmeni = Label(window, text="Příjmení", borderwidth=1, relief="solid")
    lbl_prijmeni.grid(row=0, column=2, sticky="nsew")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM `autori`")
    myresult = mycursor.fetchall()
    for i in myresult:
        rada += 1
        for r in i:
            lbl_r = Label(window, text=r, borderwidth=1, relief="solid")
            lbl_r.grid(row=rada, column=polozka, sticky="nsew")
            polozka += 1
        polozka = 0
    window.mainloop()


def seznam_k():
    global mydb
    window = nove_okno("Knihovna - seznam knih")
    rada = 0
    polozka = 0
    lbl_id = Label(window, text="ID", borderwidth=1, relief="solid")
    lbl_id.grid(row=0, column=0, sticky="nsew")
    lbl_nazev = Label(window, text="Název", borderwidth=1, relief="solid")
    lbl_nazev.grid(row=0, column=1, sticky="nsew")
    lbl_rok = Label(window, text="Rok", borderwidth=1, relief="solid")
    lbl_rok.grid(row=0, column=2, sticky="nsew")
    lbl_isbn = Label(window, text="ISBN", borderwidth=1, relief="solid")
    lbl_isbn.grid(row=0, column=3, sticky="nsew")
    lbl_id_a = Label(window, text="ID Autora", borderwidth=1, relief="solid")
    lbl_id_a.grid(row=0, column=4, sticky="nsew")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM `knihy`")
    myresult = mycursor.fetchall()
    for i in myresult:
        rada += 1
        for r in i:
            lbl_r = Label(window, text=r, borderwidth=1, relief="solid")
            lbl_r.grid(row=rada, column=polozka, sticky="nsew")
            polozka += 1
        polozka = 0
    window.mainloop()


def pridat_k():
    def zapsat_do_db(nazev, rok, isbn, id_a):
        global mydb
        rok = int(rok)
        id_a = id_a[2:-3]
        mycursor = mydb.cursor()
        mycursor.execute("SELECT id FROM `autori` WHERE prijmeni = '"+id_a+"'")
        id_a = int(mycursor.fetchone()[0])
        mycursor.execute("INSERT INTO `knihy` (`id`, `nazev`, `rok`, `isbn`, `vazba_na_autora`) VALUES (NULL, '"+nazev+"', '"+str(rok)+"', '"+isbn+"', '"+str(id_a)+"');")
        mydb.commit()
        window = nove_okno("Kniha úspěšně přidána !")
        lbl_uspech=Label(window, text="Kniha byla úspěšně přidána do databáze !", fg="green")
        lbl_uspech.pack()
    global mydb
    mycursor = mydb.cursor()
    mycursor.execute("SELECT prijmeni FROM `autori`")
    myresult = mycursor.fetchall()
    window = nove_okno("Knihovna - nová kniha")
    lbl_nadpis = Label(window, text="Přidat novou knihu", font=("Arial Bold", 20))
    lbl_nadpis.grid(row=0, columnspan=2, column=0)
    lbl_nazev = Label(window, text="Název knihy: ")
    lbl_nazev.grid(row=1, column=0)
    e_nazev = Entry(window)
    e_nazev.grid(row=1, column=1)
    lbl_rok = Label(window, text="Rok vydání: ")
    lbl_rok.grid(row=2, column=0)
    e_rok = Entry(window)
    e_rok.grid(row=2, column=1)
    lbl_isbn = Label(window, text="ISBN knihy: ")
    lbl_isbn.grid(row=3, column=0)
    e_isbn = Entry(window)
    e_isbn.grid(row=3, column=1)
    lbl_isbn = Label(window, text="Autor knihy: ")
    lbl_isbn.grid(row=4, column=0)
    variable = StringVar(window)
    variable.set(myresult[0])
    opt = OptionMenu(window, variable, *myresult)
    opt.grid(row=4, column=1)
    btn_pridat_k_do_db = Button(window, text="Přidat knihu do DB", command=lambda: zapsat_do_db(e_nazev.get(), e_rok.get(), e_isbn.get(), variable.get()))
    btn_pridat_k_do_db.grid(row=5, columnspan=2, column=0)
    window.mainloop()


def pridat_a():
    def zapsat_do_db(jmeno, prijmeni):
        global mydb
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO `autori` (`id`, `jmeno`, `prijmeni`) VALUES (NULL, '"+jmeno+"', '"+prijmeni+"'); ")
        mydb.commit()
        window = nove_okno("Autor úspěšně přidán !")
        lbl_uspech=Label(window, text="Autor byl úspěšně přidán do databáze !", fg="green")
        lbl_uspech.pack()
    window = nove_okno("Knihovna - nový autor")

    lbl_nadpis = Label(window, text="Přidat nového autora", font=("Arial Bold", 20))
    lbl_nadpis.grid(row=0, columnspan=2, column=0)
    lbl_jmeno = Label(window, text="Jméno autora ")
    lbl_jmeno.grid(row=1, column=0)
    e_jmeno = Entry(window)
    e_jmeno.grid(row=1, column=1)
    lbl_prijmeni = Label(window, text="Příjmení autora ")
    lbl_prijmeni.grid(row=2, column=0)
    e_prijmeni = Entry(window)
    e_prijmeni.grid(row=2, column=1)
    btn_pridat_a_do_db = Button(window, text="Přidat autora do DB", command=lambda: zapsat_do_db(e_jmeno.get(), e_prijmeni.get()))
    btn_pridat_a_do_db.grid(row=3, columnspan=2, column=0)
    window.mainloop()


def edit_k():
    def edit(id_k):
        def zapsat_do_db(id_knihy, novy_nazev, novy_rok, nove_isbn, nove_id_a):
            print(nove_id_a)
            mycursor = mydb.cursor()
            mycursor.execute("UPDATE `knihy` SET `nazev` = '"+novy_nazev+"', `rok` = '"+str(novy_rok)+"', `isbn` = '"+nove_isbn+"', `vazba_na_autora` = '"+nove_id_a+"' WHERE `knihy`.`id` = "+str(id_knihy)+"; ")
            mydb.commit()
            window = nove_okno("Kniha úspěšně upravena !")
            lbl_uspech = Label(window, text="Kniha byla úspěšně upravena !", fg="green")
            lbl_uspech.pack()
        global mydb
        window = nove_okno("Knihovna - editovování knihy")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM `knihy` WHERE id = '"+str(id_k)+"'")
        myresult = mycursor.fetchall()
        lbl_nadpis = Label(window, text="Editovat knihu", font=("Arial Bold", 20))
        lbl_nadpis.grid(column=0, row=0, columnspan=2)
        lbl_nazev = Label(window, text="Název knihy: ")
        lbl_nazev.grid(row=1, column=0)
        e_nazev = Entry(window)
        e_nazev.grid(row=1, column=1)
        e_nazev.insert(END, myresult[0][1])
        lbl_rok = Label(window, text="Rok vydání: ")
        lbl_rok.grid(row=2, column=0)
        e_rok = Entry(window)
        e_rok.grid(row=2, column=1)
        e_rok.insert(END, myresult[0][2])
        lbl_isbn = Label(window, text="ISBN knihy: ")
        lbl_isbn.grid(row=3, column=0)
        e_isbn = Entry(window)
        e_isbn.grid(row=3, column=1)
        e_isbn.insert(END, myresult[0][3])
        lbl_isbn = Label(window, text="ID autora knihy: ")
        lbl_isbn.grid(row=4, column=0)
        id_autora_knihy = myresult[0][4]
        mycursor = mydb.cursor()
        mycursor.execute("SELECT id FROM `autori`")
        myresult = mycursor.fetchall()
        ids = list()
        for i in myresult:
            i = str(i)[1:-2]
            ids.append(i)
        variable = StringVar(window)
        variable.set(id_autora_knihy)
        opt = OptionMenu(window, variable, *ids)
        opt.grid(row=4, column=1)
        btn_zapsat = Button(window, text="Zapsat do DB", command=lambda: zapsat_do_db(id_k, e_nazev.get(), int(e_rok.get()), e_isbn.get(), variable.get()))
        btn_zapsat.grid(row=5, columnspan=2, column=0)
    global mydb
    mycursor = mydb.cursor()
    mycursor.execute("SELECT id FROM `knihy` ")
    myresult = mycursor.fetchall()
    window = nove_okno("Knihovna - editovat knihu")
    lbl_nadpis = Label(window, text="Editovat knihu", font=("Arial Bold", 20))
    lbl_nadpis.grid(column=0, row=0, columnspan=2)
    lbl_id = Label(window, text="Vyberte ID knihy ")
    lbl_id.grid(row=1, column=0)
    variable = StringVar(window)
    variable.set(myresult[0])
    opt = OptionMenu(window, variable, *myresult)
    opt.grid(row=1, column=1)
    btn_pridat_a_do_db = Button(window, text="Editovat knihu", command=lambda: edit(variable.get()[1:-2]))
    btn_pridat_a_do_db.grid(row=2, columnspan=2, column=0)
    window.mainloop()


def edit_a():
    def edit(id_a):
        def zapsat_do_db(id_autora, nove_jmeno, nove_prijmeni):
            global mydb
            mycursor = mydb.cursor()
            mycursor.execute("UPDATE `autori` SET `jmeno` = '"+nove_jmeno+"', `prijmeni` = '"+nove_prijmeni+"' WHERE `autori`.`id` = "+str(id_autora)+";")
            mydb.commit()
            window = nove_okno("Autor úspěšně upraven !")
            lbl_uspech = Label(window, text="Autor byl úspěšně upraven !", fg="green")
            lbl_uspech.pack()
        global mydb
        window = nove_okno("Knihovna - editovování autora")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM `autori` WHERE id = "+str(id_a)+"")
        myresult = mycursor.fetchall()
        lbl_nadpis = Label(window, text="Editovat autora", font=("Arial Bold", 20))
        lbl_nadpis.grid(column=0, row=0, columnspan=2)
        lbl_jmeno = Label(window, text="Jméno autora ")
        lbl_jmeno.grid(row=1, column=0)
        e_jmeno = Entry(window)
        e_jmeno.grid(row=1, column=1)
        e_jmeno.insert(END, myresult[0][1])
        lbl_prijmeni = Label(window, text="Příjmení autora ")
        lbl_prijmeni.grid(row=2, column=0)
        e_prijmeni = Entry(window)
        e_prijmeni.grid(row=2, column=1)
        e_prijmeni.insert(END, myresult[0][2])
        btn_zapsat = Button(window, text="Zapsat do DB", command=lambda: zapsat_do_db(myresult[0][0], e_jmeno.get(), e_prijmeni.get()))
        btn_zapsat.grid(row=3, columnspan=2, column=0)
    global mydb
    mycursor = mydb.cursor()
    mycursor.execute("SELECT id FROM `autori` ")
    myresult = mycursor.fetchall()
    window = nove_okno("Knihovna - editovat autory")
    lbl_nadpis = Label(window, text="Editovat autora", font=("Arial Bold", 20))
    lbl_nadpis.grid(column=0, row=0, columnspan=2)
    lbl_id = Label(window, text="Vyberte ID autora ")
    lbl_id.grid(row=1, column=0)
    variable = StringVar(window)
    variable.set(myresult[0])
    opt = OptionMenu(window, variable, *myresult)
    opt.grid(row=1, column=1)
    btn_editovat = Button(window, text="Editovat autora", command=lambda: edit(variable.get()[1:-2]))
    btn_editovat.grid(row=2, columnspan=2, column=0)
    window.mainloop()


def smazat_k():
    def smazat_v_db(id_k):
        global mydb
        mycursor = mydb.cursor()
        mycursor.execute("DELETE FROM `knihy` WHERE `knihy`.`id` = "+str(id_k))
        mydb.commit()
        window = nove_okno("Kniha úspěšně smazána !")
        lbl_uspech=Label(window, text="Kniha byla úspěšně smazána !", fg="green")
        lbl_uspech.pack()
    global mydb
    mycursor = mydb.cursor()
    mycursor.execute("SELECT id FROM `knihy` ")
    myresult = mycursor.fetchall()
    window = nove_okno("Knihovna - smazat knihu")
    lbl_nadpis = Label(window, text="Smazat knihu", font=("Arial Bold", 20))
    lbl_nadpis.grid(column=0, row=0, columnspan=2)
    lbl_id = Label(window, text="Vyberte ID knihy ")
    lbl_id.grid(row=1, column=0)
    variable = StringVar(window)
    variable.set(myresult[0])
    opt = OptionMenu(window, variable, *myresult)
    opt.grid(row=1, column=1)
    btn_editovat = Button(window, text="Smazat knihu", command=lambda: smazat_v_db(variable.get()[1:-2]))
    btn_editovat.grid(row=2, columnspan=2, column=0)
    window.mainloop()


def smazat_a():
    def smazat_v_db(id_a):
        global mydb
        mycursor = mydb.cursor()
        mycursor.execute("DELETE FROM `autori` WHERE `autori`.`id` = "+str(id_a))
        mydb.commit()
        window = nove_okno("Kniha úspěšně smazána !")
        lbl_uspech=Label(window, text="Autor byl úspěšně smazaný !", fg="green")
        lbl_uspech.pack()
    global mydb
    mycursor = mydb.cursor()
    mycursor.execute("SELECT id FROM `autori` ")
    myresult = mycursor.fetchall()
    window = nove_okno("Knihovna - smazat autora")
    lbl_nadpis = Label(window, text="Smazat autora", font=("Arial Bold", 20))
    lbl_nadpis.grid(column=0, row=0, columnspan=2)
    lbl_id = Label(window, text="Vyberte ID autora ")
    lbl_id.grid(row=1, column=0)
    variable = StringVar(window)
    variable.set(myresult[0])
    opt = OptionMenu(window, variable, *myresult)
    opt.grid(row=1, column=1)
    btn_editovat = Button(window, text="Smazat autora", command=lambda: smazat_v_db(variable.get()[1:-2]))
    btn_editovat.grid(row=2, columnspan=2, column=0)
    window.mainloop()


def spustit_program():
    window = Tk()
    window.title("Knihovna")
    window.geometry("500x300")
    window.option_add("*font", "arial 12")
    lbl_nadpis = Label(window, text="Knihovna", font=("Arial Bold", 20))
    lbl_nadpis.pack()
    btn_seznam_k = Button(window, text="Seznam knih", command=seznam_k)
    btn_seznam_k.pack()
    btn_seznam_a = Button(window, text="Seznam autorů", command=seznam_a)
    btn_seznam_a.pack()
    btn_pridat_k = Button(window, text="Přidat novou knihu", command=pridat_k)
    btn_pridat_k.pack()
    btn_pridat_a = Button(window, text="Přidat nového autora", command=pridat_a)
    btn_pridat_a.pack()
    try:
        btn_edit_k = Button(window, text="Editovat knihu", command=edit_k)
        btn_edit_k.pack()
    except ValueError:
        window = nove_okno("Chyba !")
        lbl_uspech = Label(window, text="Rok musí být celé číslo !", fg="red")
        lbl_uspech.pack()
    btn_edit_a = Button(window, text="Editovat autora", command=edit_a)
    btn_edit_a.pack()
    btn_smazat_k = Button(window, text="Smazat knihu", command=smazat_k)
    btn_smazat_k.pack()
    btn_smazat_a = Button(window, text="Smazat autora", command=smazat_a)
    btn_smazat_a.pack()
    window.mainloop()

try:
    mydb = mysql.connector.connect(
            host="studenti.odbornaskola.cz",
            user="u304",
            passwd="2a2f10",
            database="u304",
            port="3306")
except mysql.connector.Error:
    window=nove_okno("Chyba !")
    lbl_uspech = Label(window, text="Nepodařilo se připojit do DB !", fg="red")
    lbl_uspech.pack()
spustit_program()
