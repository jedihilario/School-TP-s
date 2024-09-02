def main () -> None:
    tuple200 = ('Hilario', 'Dardo', 'Juan Manuel', 'Roman', 'Tomi')
    name = input('Que nombre queres buscar en la tupla?:\n').capitalize()
    print('El elemento si esta' if tuple200.count(name) > 0 else 'El elemento no esta')

if (__name__ == '__main__'):
    main()
