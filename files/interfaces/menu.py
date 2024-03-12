from tkinter import *
from tkinter import ttk
from .show import show_menu
from .upload import upload_menu
from .search import search_menu
from .modify import modify_menu
from db.query import Query
from models.persona import Persona

def on_quit (window: Tk, people: list[Persona]):
    Query.save_data(people)

    window.destroy()

def main_menu (window_name: str = 'Default', window_res: list[int] = [720, 360]):
    root = Tk()
    width = window_res[0]
    height = window_res[1]
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = ((root.winfo_screenheight() // 2) - (height // 2)) - 80
    root.geometry(f'{width}x{height}+{x}+{y}')
    root.title(window_name)
    root.bind('<Escape>', lambda: root.destroy())

    people_list: list[Persona] = []

    for i in Query.select_all():
        people_list.append(Persona(
            i[0], i[1], int(i[2]), int(i[3])
        ))

    frm = ttk.Frame(root, padding=10)
    frm.pack()

    title = ttk.Label(frm, font=('Helvetica', 28), text='Programa ardo de personas').pack(pady = 4)
    update = ttk.Button(frm, text = 'Cargar', command = lambda: upload_menu(root, people_list)).pack(pady = 4);
    show_button = ttk.Button(frm, text = 'Mostrar', command = lambda: show_menu(root, people_list)).pack(pady = 4)
    search_button = ttk.Button(frm, text = 'Buscar', command = lambda: search_menu(root, people_list)).pack(pady = 4)
    delete_button = ttk.Button(frm, text = 'Modificar', command = lambda: modify_menu(root, people_list)).pack(pady = 4)
    quit_button = ttk.Button(frm, text = 'Salir', command = lambda: on_quit(root, people_list)).pack(pady = 4)

    root.mainloop()