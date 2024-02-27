"""
Для задачи, в которой не указаны точные условия, необходимо использовать
максимально универсальный алгоритм сортировки.


Другие алгоритмы сортировки, такие как сортировка вставками или слиянием,
будут эффективны только для небольших массивов данных. Однако, в нашей задаче
размер массива неизвестен, поэтому такие алгоритмы могут быть неэффективными.
Сравнение будет представлено в коде.

Быстрая сортировка считается одной из самых эффективных, но она имеет несколько
недостатков. Во-первых, сложность алгоритма может увеличиться с O(n * log(n))
до O(n^2) при порядке чисел, близкому к обратному. Во-вторых, алгоритм
рекурсивный, что может привести к нерациональному использованию памяти.

Реализация быстрой сортировки на языке Python будет заведомо медленнее,
чем встроенная функция a.sort() или sorted(), т.к. она реализована на более
быстром языке программирования С++.
"""

from random import randint


def merge_sort(array: list) -> list:
    """Сортировка слиянием"""
    length = len(array)
    if length == 1:
        return array
    left = array[:(length // 2)]
    right = array[(length // 2):]
    left = merge_sort(left)
    right = merge_sort(right)
    i = 0
    j = 0
    new_array = []
    while i != len(left) and j != len(right):
        if left[i] < right[j]:
            new_array.append(left[i])
            i += 1
        else:
            new_array.append(right[j])
            j += 1
    while i != len(left):
        new_array.append(left[i])
        i += 1
    while j != len(right):
        new_array.append(right[j])
        j += 1
    return new_array


def test_merge_sort():
    print(merge_sort([7, 2, 9, 5, 4, 1]))
    print(merge_sort([1, 2, 3, 4, 5, 6]))
    print(merge_sort([6]))
    print(merge_sort([54244, 32224211, 125]))


# test_merge_sort()


def partition(array: list, left: int, right: int) -> int:
    rand = randint(left, right)
    array[rand], array[left] = array[left], array[rand]
    x = array[left]
    j = left
    for i in range(left + 1, right + 1):
        if array[i] <= x:
            j += 1
            array[j], array[i] = array[i], array[j]
    array[left], array[j] = array[j], array[left]
    return j


def quick_sort(array: list, left: int, right: int) -> None:
    if left < right:
        m = partition(array, left, right)
        quick_sort(array, left, m - 1)
        quick_sort(array, m + 1, right)
