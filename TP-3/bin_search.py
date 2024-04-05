def quicksort (arr: list[int]) -> list[int]:
    if (len(arr) < 2): return arr
    p_index: int = len(arr) - 1
    i = 0; j = len(arr) - 2

    while (i < j):
        if (arr[i] > arr[p_index] and arr[j] < arr[p_index]):
            arr[i], arr[j] = arr[j], arr[i]
        if (arr[i] < arr[p_index]): i += 1
        if (arr[j] >= arr[p_index]): j -= 1

    if (arr[i] > arr[p_index]):
        arr[i], arr[p_index] = arr[p_index], arr[i]

    return quicksort(arr[slice(0, i + 1)]) + quicksort(arr[slice(i + 1, p_index + 1)])

def bin_search (arr: list[int], target: int) -> bool:
    low = 0; top: int = len(arr) - 1
    med: int = 0

    while (low <= top):
        med: int = (low + top) // 2

        if (arr[med] == target): return True
        if (arr[med] < target): low = med + 1
        else: top = med - 1

    return False

def main () -> None:
    nums: list[int] = [4, 5, 7, 98, 4, 1, 2, 47, 9, 32]
    num: int = int(input('Que numero queres buscar en el arreglo'))
    print('Esta!' if bin_search(quicksort(nums), num) else 'No esta!')

if (__name__ == '__main__'):
    main()