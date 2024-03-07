def area (base: int, height: int):
    return (base * height) / 2
    
def main ():
    myBase = int(input('Ingrese la base del triangulo: '))
    myHeight = int(input('Ingrese la altura del triangulo: '))

    print(f'El area es: {area(myBase, myHeight)}')

if (__name__ == '__main__'):
    main()