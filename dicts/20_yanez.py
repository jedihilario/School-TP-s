def main () -> None:
    print('¿Cuantas notas queres ingresar?')
    n = int(input())
    notas = []

    for i in range(n):
        notas.append(int(input(f'Ingresa la nota {i + 1}: ')))

    histograma = {}

    for i in set(notas):
        histograma[i] = notas.count(i)

    print('El histograma final es:\n')
    print(histograma)

    print('Las apariciones da cada nota son:')

    for i in histograma:
        print(f'- {i}: {histograma[i]}')

if (__name__ == '__main__'):
    main()
