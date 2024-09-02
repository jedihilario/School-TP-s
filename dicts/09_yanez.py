def main () -> None:
    products = { 'CPU': 2000, 'GPU': 5000 , 'RAM': 1000, 'GOMIN': 10}

    for k in products:
        print(f'El precio de {k} es ${products[k]}')

if (__name__ == '__main__'):
    main()
