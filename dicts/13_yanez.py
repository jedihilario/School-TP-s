def main () -> None:
    occurrences = {}
    word = input('Ingresa la palabra para contar los caracteres: ').lower()

    for c in word:
        if (not (c in occurrences)): occurrences[c] = 1
        else: occurrences[c] += 1

    print(f'El conteo final es:\n')
    for i in occurrences:
        print(f'- {i}: {occurrences[i]}')

if (__name__ == '__main__'):
    main()
