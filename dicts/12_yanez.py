def main () -> None:
    first_student = { 'name': 'Roman', 'age': 17, 'course': 6 }
    second_student = { 'name': 'Tomito', 'age': 14, 'course': 3 }
    all_students = {}

    for k in first_student:
        all_students[k] = [first_student[k], second_student[k]]

    print(f'La informacion de todos los alumnos juntos es:\n{all_students}')

if (__name__ == '__main__'):
    main()
