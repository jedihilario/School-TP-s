def main () -> None:
    persona = {
        'nombre': 'Hilario',
        'apellido': 'YB',
        'edad': '20',
        'pelado': False
    }

    print('El diccionario en orden alfabetico es:')

    for i in sorted(persona.keys()):
        print(f'- {i}: {persona[i]}')

if (__name__ == '__main__'):
    main()