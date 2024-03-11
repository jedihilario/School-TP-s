from tkinter import *
from tkinter import ttk
from .show import show_menu
from .upload import upload_menu

def main_menu (window_name: str = 'Default', window_res: str = '720x360'):
    root = Tk()
    root.geometry(window_res)
    root.title(window_name)

    root.bind('<Escape>', lambda e: root.quit())

    frm = ttk.Frame(root, padding=10)
    frm.pack()

    title = ttk.Label(frm, font=('Helvetica', 28), text='Programa ardo de personas').pack()
    update = ttk.Button(frm, text = 'Cargar', command = lambda: upload_menu(root)).pack();
    show_button = ttk.Button(frm, text = 'Mostrar', command = show_menu).pack()
    search_button = ttk.Button(frm, text = 'Buscar', command = lambda: print('Search')).pack()
    delete_button = ttk.Button(frm, text = 'Eliminar / Modificar', command = lambda: print('Delete/modify')).pack()
    quit_button = ttk.Button(frm, text = 'Salir', command=root.destroy).pack()

    root.mainloop()