import tkinter.ttk as ttk
import sys
import hashlib

from tkinter import *
from tkinter import messagebox
from ttkbootstrap import Style
from functii.bazadedate import *

class MeniuLogin:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x350")
        self.root.title("Pykont")

        self.style = Style("flatly")

        self.label = ttk.Label(master=self.root, text="Pykont", font=("Roboto Black",24))
        self.label.pack(pady=12, padx=10)

        utilizatori = PreiaDateDinMySQL.utilizatori()
        
        self.utilizator = ttk.Entry(master=self.root)
        self.utilizator.pack(pady=12, padx=10)

        self.parola = ttk.Entry(master=self.root, show="*")
        self.parola.pack(pady=12, padx=10)

        print(utilizatori)

        async def login():
            utilizator = self.utilizator.get()
            parola = hashlib.sha256(self.parola.get().encode()).hexdigest()
            authkey = await PreiaDateDinMySQL.authkey(utilizator)

            for parola in authkey:
                if parola == authkey:
                    print("[Pykont] Autentificare reusita!")
                    messagebox.showinfo("Pykont", "Autentificare reusita!")
                else:
                    print("[Pykont] Autentificare esuata!")
                    messagebox.showerror("Pykont", "Autentificare esuata!")

        self.logare = ttk.Button(master=self.root, text="Logheaza-te", command=asyncio.run(login))
        self.logare.pack(pady=12, padx=10)

        def stop():
            self.root.destroy()
            print("[Pykont] Se inchide Pykont...")
            sys.exit()

        self.iesire = ttk.Button(master=self.root, text="Iesire", command=stop)
        self.iesire.pack(pady=12, padx=10)

        self.root.mainloop()