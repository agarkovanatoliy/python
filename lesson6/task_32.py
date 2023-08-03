# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума
# и не больше заданного максимума)
# Ввод:
# 3 4 2 5 7
# [4,6]
# Вывод:
# 1, 3


def array_filling(arr, min, max):
    resalt = []
    for i in range(len(arr)):
        if arr[i] >= min and arr[i] <= max:
            resalt.append(i)
    return resalt
list1 = [int(s) for s in input('Введите элементы списка через пробел: ').split()]
min, max = [int(s) for s in input('Введите диапазон min b max через пробел: ').split()]
list2 = array_filling(list1, min, max)

print(list2)
