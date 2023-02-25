import mysql.connector as sqlserv
from mysql.connector import Error
import json
import os
import asyncio

from tkinter import messagebox

if os.path.exists(os.getcwd() + "./config/config.json"):
    with open ("./config/config.json")as f:
        configData = json.load(f)
else:
    DefaultConfig = {
        "host": "localhost",
        "nume_bd": "pykont", 
        "utilizator_bd": "pykont",
        "parola_bd": ""
    }
    with open (os.getcwd() + "/config/config.json", "w+") as f:
        json.dump(DefaultConfig, f)


class ConectareLaMySQL:
    async def mysql():
        print("[Pykont] Se verifica conexiunea la baza de date...")
        try:
            conexiuneBaza = sqlserv.connect(
                host=configData["host"],
                user=configData["utilizator_bd"],
                password=configData["parola_bd"],
                database=configData["nume_bd"]
            )

            if conexiuneBaza.is_connected():
                bdInfo = conexiuneBaza.get_server_info()
                print("[Pykont] Conectat la serverul MySQL versiunea", bdInfo)

        except Error as e:
            messagebox.showerror("Pykont", "Eroare! Nu ma pot conecta la baza de date...")
            print("[Pykont] Eroare! Nu ma pot conecta la baza de date:", e)
            print("[Pykont] Pykont se va inchide datorita unei erori la baza de date!")
            exit()

class PreiaDateDinMySQL:
    async def utilizatori():

        utilizatori = []

        try:
            conexiuneBaza = sqlserv.connect(
                host=configData["host"],
                user=configData["utilizator_bd"],
                password=configData["parola_bd"],
                database=configData["nume_bd"]
            )

            if conexiuneBaza.is_connected():
                cursor = conexiuneBaza.cursor()
                cursor.execute("SELECT utilizator FROM utilizatori")
                utilizatori = cursor.fetchall()

                # only keep the text without any symbols
                utilizatori = [str(i).replace("('", "").replace("',)", "") for i in utilizatori]

                print("[Pykont] Am preluat datele din baza de date cu succes!")
                return utilizatori
                
        except Error as e:
            messagebox.showerror("Pykont", "Eroare! Nu ma pot conecta la baza de date...")
            print("[Pykont] Eroare! Nu ma pot conecta la baza de date:", e)
            print("[Pykont] Pykont se va inchide datorita unei erori la baza de date!")
            exit()

    async def authkey(utilizator):
        try:
            conexiuneBaza = sqlserv.connect(
                host=configData["host"],
                user=configData["utilizator_bd"],
                password=configData["parola_bd"],
                database=configData["nume_bd"]
            )

            if conexiuneBaza.is_connected():
                cursor = conexiuneBaza.cursor()
                cursor.execute("SELECT authkey FROM utilizatori WHERE utilizator = %s", (utilizator,))
                authkey = cursor.fetchone()
                authkey = str(authkey).replace("('", "").replace("',)", "")

                print("[Pykont] Am preluat datele din baza de date cu succes!")
                return authkey
                
        except Error as e:
            messagebox.showerror("Pykont", "[Pykont] Eroare:" + e)
            print("[Pykont] Eroare:", e)
            print("[Pykont] Pykont se va inchide datorita unei erori la baza de date!")
            exit()

class IncearcaLogin:
    async def login(utilizator, authkey):
        try:
            conexiuneBaza = sqlserv.connect(
                host=configData["host"],
                user=configData["utilizator_bd"],
                password=configData["parola_bd"],
                database=configData["nume_bd"]
            )
            
            cursor = conexiuneBaza.cursor()
            cursor.execute("SELECT * FROM utilizatori WHERE utilizator = %s AND authkey = %s", (utilizator, authkey))
            utilizator = cursor.fetchone()
            if utilizator:
                messagebox.showinfo("Pykont", "Utilizatorul a fost autentificat cu succes!")
                print("[Pykont] Utilizatorul a fost autentificat cu succes!")
                return True
            else:
                messagebox.showerror("Pykont", "Utilizatorul nu a fost autentificat!")
                print("[Pykont] Utilizatorul nu a fost autentificat!")
                return False
            
        except Error as e:
            messagebox.showerror("Pykont", "Eroare! Nu ma pot conecta la baza de date...")
            print("[Pykont] Eroare! Nu ma pot conecta la baza de date:", e)
            print("[Pykont] Pykont se va inchide datorita unei erori la baza de date!")
            exit()

# Debug lol
# parola = PreiaDateDinMySQL.authkey("user")
# if asyncio.run(parola) == "user2":
#     print("true")
# else:
#     print("false")
