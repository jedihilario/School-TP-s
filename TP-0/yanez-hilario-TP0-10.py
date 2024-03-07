def concat_strings (first_word: str, second_word: str):
    return first_word + second_word

def main ():
    first = input('Ingresa la primer palabra: ')
    second = input('Ingresa la segunda palabra: ')
    print(f'La concatenacion es: {concat_strings(first, second)}')

if (__name__ == '__main__'):
    main()