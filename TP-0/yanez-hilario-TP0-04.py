def main ():
    res: int = 0
    i: int = 5

    while (i > 0):
        res += i
        i -= 1

    print(f'La suma de los primeros 5 naturales es: {res}')

if (__name__ == '__main__'):
    main()