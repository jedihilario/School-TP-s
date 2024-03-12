from tkinter import *
from tkinter import ttk
from models.persona import Persona

def show_menu (parent: Tk, people: list[Persona]) -> None:
    window = Toplevel(parent)
    window.geometry('720x360')
    window.title('Mostrar personas')

    content = ''

    for i in people:
        content += f'Nombre: {i.name} | Apellido: {i.surname} | DNI: {i.dni} | Edad: {i.age}\n\n'

    ttk.Label(window, text = content, font = ('Helvetica', 16)).pack(pady = 2)
    ttk.Button(window, text = 'Volver', command = lambda: window.destroy()).pack(pady = 2)

    window.focus()