from models.persona import Persona

def search (people: list[Persona], name: str) -> str:
    result = 'Resultado:\n'

    for i in people:
        if (i.name == name):
            result += f'Nombre: {i.name} | Apellido: {i.surname} | DNI: {i.dni} | Edad: {i.age}\n\n'

    return result