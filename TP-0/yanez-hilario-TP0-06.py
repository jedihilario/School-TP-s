def main ():
    num: int = int(input('Ingresa el numero para calcular el factorial: '))
    res: int = 1

    res *= num
    num -= 1

    while (num > 1):
        res *= num
        num -= 1

    print(res)

if (__name__ == '__main__'):
    main()