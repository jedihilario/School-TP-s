def main () -> None:
    c = {}
    phrase = input('Ingresa la oracion:\n')

    for i in phrase.split(' '):
        if (i in c): c[i] += 1
        else: c[i] = 1

    print('El conteo de palabras es el siguiente:')

    for i in c:
        print(f'- {i}: {c[i]}')

if (__name__ == '__main__'):
    main()