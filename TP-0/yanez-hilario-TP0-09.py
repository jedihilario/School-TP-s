from math import trunc

def main ():
    int_num: int = int(input('Ingresa un numero entero: '))
    float_num: float = float(input('Ingresa un numero decimal (punto flotante): '))
    float_res: float = float(int_num + float_num)
    int_res: int = int(int_num + float_num)

    print(f'El resultado entero es {int_res}')
    print(f'El resultado decimal es ~{"{:.2f}".format(float_res)}')

if (__name__ == '__main__'):
    main()