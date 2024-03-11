from tkinter import *
from tkinter import ttk

def main_menu (window_name: str = 'Default', window_res: str = '720x360'):
    root = Tk()
    root.geometry(window_res)
    root.title(window_name)

    frm = ttk.Frame(root, padding=10)
    frm.pack()
    # frm.grid()

    title = ttk.Label(frm, font=('Helvetica', 28), text='Programa ardo de personas').pack()
    update = ttk.Button(frm, text = 'Cargar', command = lambda: print('Cargar')).pack();
    show_button = ttk.Button(frm, text = 'Mostrar', command = lambda: print('show')).pack()
    search_button = ttk.Button(frm, text = 'Buscar', command = lambda: print('Search')).pack()
    delete_button = ttk.Button(frm, text = 'Eliminar / Modificar', command = lambda: print('Delete/modify')).pack()
    quit_button = ttk.Button(frm, text = 'Salir', command=root.destroy).pack()

    root.mainloop()