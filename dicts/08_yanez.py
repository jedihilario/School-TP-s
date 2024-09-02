def main () -> None:
    contact = { 'mail': 'daguilera@200.com', 'phone': '1234567890', 'telegraph': None }
    key = input('Ingresa la clave a buscar: ')

    if (key in contact.keys()):
        print(f'El valor de {key} es: {contact[key]}')
    else:
        print('Esa clave no esta en el contacto!')

if (__name__ == '__main__'):
    main()
