from tkinter import *
from tkinter import ttk
from models.persona import Persona
from utils.search import search_by_dni

def modify (people: list[Persona], dni: IntVar, new_data: map, op_var: StringVar) -> None:
    try:
        dni = dni.get()
        new_data['name'] = new_data['name'].get()
        new_data['surname'] = new_data['surname'].get()
        new_data['dni'] = new_data['dni'].get()
        new_data['age'] = new_data['age'].get()

        if (new_data['dni'] < 0 or new_data['age'] < 0): raise Exception()
    except:
        op_var.set('Error: Datos invalidos'); return
    
    index = search_by_dni(people, dni)

    if (index == -1): op_var.set('Error: Persona no encontrada'); return


    if (new_data['name'] == ''): new_data['name'] = people[index].name
    if (new_data['surname'] == ''): new_data['surname'] = people[index].surname
    if (new_data['dni'] == 0): new_data['dni'] = people[index].dni
    if (new_data['age'] == 0): new_data['age'] = people[index].age

    people[index].name = new_data['name']
    people[index].surname = new_data['surname']
    people[index].dni = new_data['dni']
    people[index].age = new_data['age']

    op_var.set('Exito')

def modify_menu (parent: Tk, people: list[Persona]):
    window: Toplevel = Toplevel(parent)
    window.geometry('720x360')
    window.title('Modificar persona')

    op_msg = StringVar()

    ttk.Label(window, text = 'DNI de la persona a modificar:').pack(pady = 2)
    search_var = IntVar()
    search_entry = ttk.Entry(window, textvariable = search_var).pack(pady = 2)
    ttk.Label(window, text = 'Nuevo nombre:').pack(pady = 2)
    new_name = StringVar()
    name_entry = ttk.Entry(window, textvariable = new_name).pack(pady = 2)
    ttk.Label(window, text = 'Nuevo apellido:').pack(pady = 2)
    new_surname = StringVar()
    surname_entry = ttk.Entry(window, textvariable = new_surname).pack(pady = 2)
    ttk.Label(window, text = 'Nuevo DNI:').pack(pady = 2)
    new_dni = IntVar()
    dni_entry = ttk.Entry(window, textvariable = new_dni).pack(pady = 2)
    ttk.Label(window, text = 'Nueva edad:').pack(pady = 2)
    new_age = IntVar()
    age_entry = ttk.Entry(window, textvariable = new_age).pack(pady = 2)
    ttk.Button(window, text = 'Modificar', command = lambda: modify(people, search_var, {
        'name': new_name, 'surname': new_surname, 'dni': new_dni, 'age': new_age
    }, op_msg)).pack(pady = 2)
    ttk.Button(window, text = 'Cancelar', command = lambda: window.destroy()).pack(pady = 2)
    ttk.Label(window, textvariable = op_msg, font = ('Helvetica', 14)).pack(pady = 2)