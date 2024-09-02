def main () -> None:
    materias = {
        'matematica': [1, 5, 5, 4, 6],
        'lengua': [7, 8, 5, 10, 10],
        'programacion': [1, 1, 1, 1],
        'ingles': [10, 10, 10, 9]
    }

    for m in materias:
        print(f'El promedio de {m} es de {sum(materias[m]) / len(materias[m])}')

if (__name__ == '__main__'):
    main()
