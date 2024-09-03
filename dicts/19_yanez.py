def main () -> None:
    coords = {
        (0, 0): 'Origen',
        (1, 2): 'Casa de Juan Manuel',
        (200, 200): 'Casa de Dardo Aguilera',
        (-1, -2): 'Holmberg'
    }

    c = (int(input('Ingresa la primer coordenada: ')), int(input('Ingresa la segunda coordenada: ')))
    if (c in coords):
        print(f'En las coordenadas {c} esta "{coords[c]}"')
    else:
        print('En esas coordenadas no hay nada identificado')

if (__name__ == '__main__'):
    main()
