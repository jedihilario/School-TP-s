from tkinter import *
from tkinter import ttk

def upload_menu (parent) -> None:
    upload_root = Toplevel(parent)
    upload_root.geometry('720x360')
    upload_root.title('Cargar persona')

    ttk.Label(upload_root, text = 'Nombre: ').pack()
    ttk.Entry(upload_root).pack()
    ttk.Label(upload_root, text = 'Apellido: ').pack()
    ttk.Entry(upload_root).pack()
    ttk.Label(upload_root, text = 'DNI: ').pack()
    ttk.Entry(upload_root).pack()
    ttk.Label(upload_root, text = 'Edad: ').pack()
    ttk.Entry(upload_root).pack()