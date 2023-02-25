import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import mysql.connector as sqlserv
from mysql.connector import Error
import os
import json

from tkinter import messagebox

def valideaza_denumire(x) -> bool:
    # verifica daca xa este un sir de text
    if x.isdigit():
        return False
    elif x == "":
        return True
    else:
        return True

def valideaza_numar(x) -> bool:
    # verifica dacad x este un numar
    if x.isdigit():
        return True
    elif x == "":
        return True
    else:
        return False

root = tk.Tk()
root.geometry("1024x768")

functie_numar = root.register(valideaza_numar)
functie_text = root.register(valideaza_denumire)

label = ttk.Label(master=root, text="Configurator Societati", font=("Roboto Black",24))
label.pack(pady=6, padx=10)

labelDenumire = ttk.Label(root, text="Denumire").pack()
denumire = ttk.Entry(master=root, validate="focus", validatecommand=(functie_text, '%P'))
denumire.pack(pady=12, padx=0)

labelCF = ttk.Label(root, text="Cod Fiscal").pack()
codfiscal = ttk.Entry(master=root, validate="focus", validatecommand=(functie_numar, '%P'))
codfiscal.pack(pady=12, padx=10)

labelRC = ttk.Label(root, text="Nr. inreg. RC").pack()
nrregcomert = ttk.Entry(master=root, validate="focus", validatecommand=(functie_text, '%P'))
nrregcomert.pack(pady=12, padx=10)

labelJudet = ttk.Label(root, text="Judet").pack()
listajudete = []
# from localitati.json add to listajudete all values called "judet"
with open('./config/localitati.json') as f:
    data = json.load(f)
    for i in data:
        listajudete.append(i["judet"])
# remove duplicates from listajudete
judete = list(dict.fromkeys(listajudete))
judete.sort()

judet = ttk.Combobox(master=root, values=tuple(judete))
judet.pack(pady=12, padx=10)


# from localitatii.json add to localitati all values called "nume" where "judet" is equal to the value selected in the combobox above
def selectjudet(event):
    localitati = []
    with open('./config/localitati.json') as f:
        data = json.load(f)
        for i in data:
            if i["judet"] == judet.get():
                localitati.append(i["nume"])
    localitati.sort()
    localitate.config(values=tuple(localitati))

judet.bind("<<ComboboxSelected>>", selectjudet)

labelLocalitate = ttk.Label(root, text="Localitate").pack()
localitate = ttk.Combobox(master=root)
localitate.pack(pady=12, padx=10)

labelAdresa = ttk.Label(root, text="Adresa").pack()
adresa = ttk.Entry(master=root, validate="focus", validatecommand=(functie_text, '%P'))
adresa.pack(pady=12, padx=10)

labelTelefon = ttk.Label(root, text="Telefon").pack()
telefon = ttk.Entry(master=root, validate="focus", validatecommand=(functie_numar, '%P'))
telefon.pack(pady=12, padx=10)

labelMail = ttk.Label(root, text="Mail").pack()
mail = ttk.Entry(master=root, validate="focus", validatecommand=(functie_text, '%P'))
mail.pack(pady=12, padx=10)

class ConfiguratorSocietati:

    def __init__(self):
        self = self

    # add to database values from the entries above
    def adaugasocietate(self):
        try:
            conectareBD = sqlserv.connect(host='localhost', database='db', user='user', password='password')
            if conectareBD.is_connected():
                cursor = conectareBD.cursor()
                cursor.execute("INSERT INTO societati (denumire, codfiscal, nrregcomert, localitate, judet, adresa, telefon, mail) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (denumire.get(), codfiscal.get(), nrregcomert.get(), localitate.get(), judet.get(), adresa.get(), telefon.get(), mail.get()))
                conectareBD.commit()
                messagebox.showinfo("Succes", "Societatea a fost adaugata!")
                cursor.close()
        except Error as e:
            messagebox.showinfo("Eroare", "Societatea nu a putut fi adaugata!")
    
root.mainloop()