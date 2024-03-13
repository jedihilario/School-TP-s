from tkinter import *
from tkinter import ttk
from models.persona import Persona

def add_person (window: Toplevel, people_list: list[Persona], new_data: map):
    people_list.append(Persona(
        new_data['name'].upper(), new_data['surname'].upper(), new_data['dni'], new_data['age']
    ))

    window.destroy()

def check (window: Toplevel, people_list: list[Persona], new_data: map, err_msg: StringVar) -> None:
    try:
        add_person(window, people_list, {
            'name': new_data['name'].get(), 'surname': new_data['surname'].get(), 'dni': new_data['dni'].get(), 'age': new_data['age'].get()
        })
    except:
        err_msg.set('Error: Datos invalidos')

def upload_menu (parent: Tk, people_list: list[Persona]) -> None:
    upload_root = Toplevel(parent)
    upload_root.geometry('720x360')
    upload_root.title('Cargar persona')

    err = StringVar()

    ttk.Label(upload_root, text = 'Nombre: ').pack(pady = 2)
    name_var = StringVar()
    name_entry = ttk.Entry(upload_root, textvariable = name_var).pack(pady = 2)
    ttk.Label(upload_root, text = 'Apellido: ').pack(pady = 2)
    surname_var = StringVar()
    surname_entry = ttk.Entry(upload_root, textvariable = surname_var).pack(pady = 2)
    ttk.Label(upload_root, text = 'DNI: ').pack(pady = 2)
    dni_var = IntVar()
    dni_entry = ttk.Entry(upload_root, textvariable = dni_var).pack(pady = 2)
    ttk.Label(upload_root, text = 'Edad: ').pack(pady = 2)
    age_var = IntVar()
    age_entry = ttk.Entry(upload_root, textvariable = age_var).pack(pady = 2)
    ttk.Button(upload_root, text = 'Cargar', command = lambda: check(upload_root, people_list, {
        'name': name_var, 'surname': surname_var, 'dni': dni_var, 'age': age_var
    }, err)).pack(pady = 2)
    ttk.Button(upload_root, text = 'Cancelar', command = lambda: upload_root.destroy()).pack(pady = 2)
    ttk.Label(upload_root, textvariable = err, font = ('Helvetica', 14)).pack(pady = 4)

    upload_root.focus()