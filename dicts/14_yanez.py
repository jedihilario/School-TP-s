def main () -> None:
    empleados = {
        'dardo': {
            'cargo': 'profesor',
            'salario': 'mucho 😎'
        },
        'roman': {
            'cargo': 'granjero',
            'salario': 100
        },
        'juan manuel': {
            'cargo': 'team lead',
            'salario': 2000
        }
    }

    name = input('Ingresa el nombre a buscar: ').lower()

    if (not name in empleados):
        print(f'{name} no esta en la lista')
    else:
        print(f'Los datos de {name} son:')
        for k in empleados[name]:
            print(f'- {k}: {empleados[name][k]}')

if (__name__ == '__main__'):
    main()
