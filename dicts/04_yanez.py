def main () -> None:
    student = { 'nombre': 'Roman', 'curso': 6, 'edad': 17 }
    new_age = int(input('Ingresa la nueva edad del estudiante: '))
    student['edad'] = new_age
    print(f'El diccionario resultante es: {student}')

if (__name__ == '__main__'):
    main()
