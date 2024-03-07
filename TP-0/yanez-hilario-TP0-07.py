def isPrime (num: int):
    for i in range(2, num // 2 + 1):
        if (num % i == 0): return False
    return True

def main ():
    num: int = int(input('Ingresa el numero para saber si es primo: '))
    print(f'{'Es primo!' if isPrime(num) else 'No es primo :('}')

if (__name__ == '__main__'):
    main()