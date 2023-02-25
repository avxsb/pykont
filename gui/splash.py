import tkinter as tk
from time import sleep

def task():
    sleep(2)
    root.destroy()

root = tk.Tk()
root.title("Pykont")

label = tk.Label(root, text="SE INCARCA FISIERELE... NU INCHIDE!")
label.pack()

root.after(200, task)
root.mainloop()

print("Main loop is now over and we can do other stuff.")