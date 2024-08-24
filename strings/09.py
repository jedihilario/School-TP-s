def main ():
    word = input('Ingresa una oracion: ')
    words = word.split(' ')

    for i in range(len(words)):
        print(f'La {i + 1} palabra es: {words[i]}')

if (__name__ == '__main__'):
    main()
