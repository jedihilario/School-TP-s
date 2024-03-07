def isEven (num: int):
    return num % 2 == 0

def main ():
    num = int(input('Ingresa un numero: '))
    print(f'{'Es par!' if isEven(num) else 'Es impar :('}')

if (__name__ == '__main__'):
    main()