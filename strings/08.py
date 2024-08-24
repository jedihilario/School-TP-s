def main ():
    word = input('Ingresa una oracion: ')
    replaced = input('Ingresa la palabra a reemplazar: ')
    replacer = input('Ingresa la nueva palabra: ')

    word = word.replace(replaced, replacer)

    print(f'La nueva oracion es: "{word}"')

if (__name__ == '__main__'):
    main()
