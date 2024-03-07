def main ():
    array: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(len(array)):
        if (array[i] % 2 == 0):
            array[i] *= 2

    for i in array: print(i)

if (__name__ == '__main__'):
    main()