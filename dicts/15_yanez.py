def main () -> None:
    numbers = ['1', "4", '2', '6', '6', '3', '1', '8']
    c = {}

    for i in numbers:
        if (not (i in c)): c[i] = 1
        else: c[i] += 1
    
    res = []
    for k in c.keys():
        if (c[k] == 1): res.append(k)

    print(f'La lista sin duplicados es: {res}')

if (__name__ == '__main__'):
    main()
