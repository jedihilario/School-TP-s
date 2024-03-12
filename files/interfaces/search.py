from tkinter import *
from tkinter import ttk
from models.persona import Persona
from utils.search import search_by_name

def search_menu (parent: Tk, people: list[Persona]) -> None:
    window = Toplevel(parent)
    window.geometry('720x360')
    window.title('Buscar persona')

    result: StringVar = StringVar()

    ttk.Label(window, text = 'Ingresa el nombre a buscar:').pack(pady = 2)
    search_var = StringVar()
    search_entry = ttk.Entry(window, textvariable = search_var).pack(pady = 2)
    ttk.Button(window, text = 'Buscar', command = lambda: result.set(search_by_name(people, search_var.get())[0])).pack(pady = 2)
    ttk.Button(window, text = 'Salir', command = lambda: window.destroy()).pack(pady = 2)
    ttk.Label(window, font = ('Helvetica', 12),textvariable = result).pack(pady = 4)