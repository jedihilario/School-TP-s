def main ():
    word = input('Ingresa una palabra: ')
    letter = input('Ingresa la letra para contar: ')
    c = word.lower().count(letter)

    print(f'La letra {letter} aparece {c} veces en la palabra "{word}"')

if (__name__ == '__main__'):
    main()
