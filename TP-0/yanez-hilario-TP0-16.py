class Persona:
    def __init__(self, name: str = 'Dardo', age: int = 0) -> None:
        self.name = name
        self.age = age

def main ():
    hilario = Persona('Hilario', 17)
    juan = Persona('Juan') # age toma el valor 0 por falta del parametro
    dardo = Persona() # nombre toma 'Dardo' y edad 0 por parametros por defecto

    print(f'Nombres:\nHilario: {hilario.name}, Juan: {juan.name}, Dardo: {dardo.name}')
    print(f'Edades:\nHilario: {hilario.age}, Juan: {juan.age}, Dardo: {dardo.age}')

if (__name__ == '__main__'):
    main()