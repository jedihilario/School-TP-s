def main ():
    matrix: list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    sum: int = 0

    for i in range(len(matrix)):
        sum += matrix[i][i]

    print(sum) # Deberia ser 1 + 5 + 9 => 15

if (__name__ == '__main__'):
    main()