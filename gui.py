import tkinter as tk
from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=300)
frm.grid()
ttk.Label(frm, text="Hello, GUI!").grid(column=0, row=0)
ttk.Button(frm, text="Exit", command=root.destroy).grid(column=0, row=2)
ttk.Button(frm, text="Play").grid(column=0, row=1)
root.mainloop()

pip install pygame_gui