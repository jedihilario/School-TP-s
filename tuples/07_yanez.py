def main () -> None:
    tuple200 = ((100, 200, 300), (400, 500, 600))

    print('Los elementos de la tupla son los siguientes:')

    for i in tuple200:
        for j in i:
            print(f'- {j}')

if (__name__ == '__main__'):
    main()
