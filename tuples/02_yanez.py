def main () -> None:
    tuple200 = tuple([i for i in range(1, 21)])
    print('La tupla creada contiene los numeros del 1 al 20')
    print(f'El segundo elemento es el {tuple200[1]} y el penultimo es el {tuple200[-2]}')    

if (__name__ == '__main__'):
    main()
