def main () -> None:
    tuple200 = ('D', 'a', 'r', 'd', 'o', '2', '0', '0')
    print(f'La tupla {tuple200} convertida a string es la siguiente:')
    print(str(tuple200).replace('(', '').replace(')', '').replace(' ', '').replace("'", '').replace(',', ''))

if (__name__ == '__main__'):
    main()
