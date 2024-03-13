from models.persona import Persona

def search_by_name (people: list[Persona], name: str) -> list[str, int]:
    result: list[str, int] = ['Resultado:\n', 0]
    name = name.upper()

    for i, person in enumerate(people):
        if (person.name == name):
            result[0] += f'Nombre: {person.name} | Apellido: {person.surname} | DNI: {person.dni} | Edad: {person.age}\n\n'
            result[1] = i

    if (result[0] == 'Resultado:\n'): result[0] = 'No se encontro :('

    return result

def search_by_dni (people: list[Persona], dni: int) -> int:
    result = -1

    for i, person in enumerate(people):
        if (person.dni == dni):
            result = i; break
        
    return result