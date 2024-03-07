from math import pi

def circ_area (radio: int): return pi * radio * radio

def main ():
    radio: int = int(input('Ingresa el radio del circulo: '))
    print(f'El area del circulo es: ~{'{:.2f}'.format(circ_area(radio))}')

if (__name__ == '__main__'):
    main()