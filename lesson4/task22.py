# Задача 22: Даны два неупорядоченных набора целых чисел (может быть,
# с повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.


n = int(input('Введите длинну первого множества -> '))
m = int(input('Введите длинну второго множества -> '))

n_set = set()
m_set = set()

i = 1
while i <= n:
    a = int(input(f'Введите {i} элемент первого множества -> '))
    n_set.add(a)
    i += 1

i = 1
while i <= m:
    a = int(input(f'Введите {i} элемент второго множества -> '))
    m_set.add(a)
    i += 1

n_set.update(m_set)
print(sorted(n_set))