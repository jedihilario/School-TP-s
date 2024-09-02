def main () -> None:
    students = ['Hilario', 'Juan', 'Tomi', 'Roman']
    grades = [[1, 1, 1, 1], [10, 10, 10, 10], [8, 7, 9, 9], [2, 3, 8, 5]]

    diccionario = {}
    for i in range(len(students)):
        diccionario[students[i]] = grades[i]

    print(f'Diccionario final:')
    print(diccionario)

if (__name__ == '__main__'):
    main()