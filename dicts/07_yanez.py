def main () -> None:
    countries = { 'Argentina': 'Buenos Aires', 'Chile': 'Santiago', 'Bolivia': 'La Paz', 'Brasil': 'Brasilia', 'Uruguay': 'Montevideo' }
    for country in countries.keys():
        print(f'{countries[country]} es la capital de {country}')

if (__name__ == '__main__'):
    main()
