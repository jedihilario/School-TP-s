def main () -> None:
    person = {}
    name = input('Ingresa el nombre a agregar: ')
    person['nombre'] = name
    print(f'El diccionario resultante es: {person}')

if (__name__ == '__main__'):
    main()
