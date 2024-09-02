def main () -> None:
    book = { 'title': 'Las penas del pe...', 'author': 'Tomito', 'year': 2024 }
    del book['year']
    print(f'El diccionario resultante es: {book}')

if (__name__ == '__main__'):
    main()
