def main () -> None:
    tuple200 = tuple([i for i in range(1, 6)])
    print(f'La tupla creada es la siguiente:\n{tuple200}')
    print('Los elementos de la tupla son:')
    for i in tuple200: print(f'- {i}')

if (__name__ == '__main__'):
    main()
