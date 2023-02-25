import tkinter as tk
import ttkbootstrap as ttk

from ttkbootstrap.constants import *
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x350")

frame = ttk.Frame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = ttk.Label(master=frame, text="Configurator societati", font=("Roboto Black",24))
label.pack(pady=12, padx=10)
listasocietati = ttk.Combobox(master=frame, values=societati)
listasocietati.pack(pady=12, padx=10)
listasocietati.set("Societate")

button = ttk.Button(master=frame, text="Editor societati", command=scnou)
button.pack(pady=12, padx=10)


button = ttk.Button(master=frame, text="Catre login", command=societateselectata)
button.pack(pady=12, padx=10)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()