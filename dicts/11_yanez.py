def main () -> None:
    og = { 'nombre': 'dardo200', 'edad': 'la suficiente', 'poder': 'incalculable', 'apodo': 'la eminencia' }
    print(f'El diccionario original es: {og}')

    new = {}

    for k in og:
        new[og[k]] = k

    print(f'El nuevo diccionario es {new}')

if (__name__ == '__main__'):
    main()
