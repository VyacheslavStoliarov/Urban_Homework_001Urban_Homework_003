data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
# Первый вариант
def calculate_structure_sum(a):
    sum = 0
    ss = str(a)
    p = '[]{}() '
    for i in p:
        ss = ss.replace(i, '')
    ss = ss.replace(':', ',')
    ss = ss.split(',')
    for i in ss:
        if i.isdigit():
            sum += int(i)
        else:
            if len(i) > 0:
                sum += int(len(i)-2)
    return sum

result = calculate_structure_sum(data_structure)
print(result)
print('*******************')

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
# Второй вариант
def calculate_structure_sum(a, temp=[0]):
    # Перебираем список поэлементно, берем первый элемент - проверяем, удаляем.
    # Если элемент это строка, то считаем длину и получаем вместо строки число
    if isinstance(a[0], str):
        a[0] = len(a[0])
    # если элемент это число, то считаем сумму в первом элементе списка temp
    if isinstance(a[0], int):
        temp[0] += a[0]
    # если массив
    else:
        # если массив это словарь, то вытаскиваем ключ и значение как отдельные элементы
        if isinstance(a[0], dict):
            for key, val in a[0].items():
                temp.append(key)
                temp.append(val)
        # если просто массив, то вытаскиваем каждый элемент
        else:
            for i in a[0]:
                temp.append(i)
    # Элемент проверен и записан в список. Можно удалять
    a.pop(0)
    # перебираем пока исходный список не кончится
    if len(a) > 0:
        return calculate_structure_sum(a, temp)
    # исходный список кончился, но сумма еще не посчитана (список не из одного элемента)
    elif len(temp) > 1:
        return calculate_structure_sum(temp, [0])
    # сумма посчитана. список из одного элемента. Вывести только значение
    else:
        return temp[0]
result = calculate_structure_sum(data_structure)
print(result)