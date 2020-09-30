"""
Different sorting algorithms
"""


def selection_sort(arr):
    """
    Selection sort algorithm

    :param arr: array to be sorted
    :return: number of comparisons
    """
    comparisons = 0
    for i in range(len(arr)):

        min_idx = i

        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[min_idx] > arr[j]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return comparisons


def insertion_sort(arr):
    """
    Insertion sort algorithm

    :param arr: array to be sorted
    :return: number of comparisons
    """
    comparisons = 0
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        comparisons += 1
        while j >= 0 and key < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return comparisons


def merge_sort(arr, comparisons=0):
    """
    Merge sort algorithm

    :param comparisons: comparisons counter (to avoid global vars)
    :param arr: array to be sorted
    :return: number of comparisons
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        comp_l = merge_sort(L, comparisons)
        comp_r = merge_sort(R, comparisons)
        comparisons += comp_l + comp_r
        i = j = k = 0

        while i < len(L) and j < len(R):
            comparisons += 1
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
    return comparisons


def shell_sort(arr):
    """
    Shell sort algorithm

    :param arr: array to be sorted
    :return: number of comparisons
    """
    comparisons = 0
    n = len(arr)
    gap = n // 2

    while gap > 0:

        for i in range(gap, n):

            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                comparisons += 1
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2
    return comparisons