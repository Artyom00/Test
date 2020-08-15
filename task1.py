"""
### Задача

Нужно выполнить следующие действия и вывести результат вычислений:

1. Отсортировать все имена в лексикографическом порядке.
2. Посчитать для каждого имени алфавитную сумму – сумму порядковых номеров букв (MAY: 13 + 1 + 25 = 39).
3. Умножить алфавитную сумму каждого имени на порядковый номер имени
в отсортированном списке (индексация начинается с 1).
Например, если MAY находится на 63 месте в списке, то результат для него будет 63 * 39 = 2457.
4. Сложить произведения из п. 3 для всех имен из файла и получить число.
5. Вывести полученную сумму.
"""

try:
    with open('names.txt') as file_obj:
        data = file_obj.read().split(',')
except Exception as ex:
    print(ex)

names_list = []

costs_dict = {
    'A': 1, 'B': 2, 'C': 3,
    'D': 4, 'E': 5, 'F': 6,
    'G': 7, 'H': 8, 'I': 9,
    'J': 10, 'K': 11, 'L': 12,
    'M': 13, 'N': 14, 'O': 15,
    'P': 16, 'Q': 17, 'R': 18,
    'S': 19, 'T': 20, 'U': 21,
    'V': 22, 'W': 23, 'X': 24,
    'Y': 25, 'Z': 26
}

sum_dict = {}

for i in range(len(data)):
    temp = data[i].replace('"', '')
    names_list.append(temp)

names_list.sort()

_sum = 0
for index, name in enumerate(names_list):
    index += 1
    for symbol in name:
        _sum += costs_dict[symbol]
    _sum *= index
    sum_dict[name] = _sum
    print(f'position: {index} name: {name} value: {_sum}')
    _sum *= 0

total = 0
for cost in sum_dict:
    total += sum_dict[cost]

print()
print('The total amount is ' + str(total))


