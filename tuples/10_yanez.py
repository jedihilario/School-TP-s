def main () -> None:
    tuple200 = (1, 34, 5, 5, 3, 2, 9, 5, 1)
    e = int(input('Ingresa el numero a buscar en la tupla: '))
    print(f'El numero {e} aparece {tuple200.count(e)} veces en la tupla')

if (__name__ == '__main__'):
    main()
