# Найти сумму чисел списка стоящих на нечетной позиции
import random
def get_sum(list):
    sum = 0
    for i in range(1, len(list), 2):
        sum += list[i]
    return sum


print(get_sum([1, 2, 3, 4, 5, 6, 7, 8, 9]))
# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]
def get_product(list):
    left, right, product, prod_list = 0, len(list) - 1, 0, []
    while left <= right:
        product = list[left] * list[right]
        prod_list.append(product)
        left += 1
        right -= 1
    return prod_list


print(get_product([2, 3, 4, 5, 6]))
print(get_product([2, 3, 5, 6]))
# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
def get_diff(list):
    max_part = 0
    min_part = 1
    for i in list:
        max_part = max(max_part, i % 1)
        min_part = min(min_part, (1 if i % 1 == 0 else i % 1))
    return max_part - min_part

print(get_diff([1.1, 1.2, 3.1, 5, 10.01]))
# Написать программу преобразования десятичного числа в двоичное
def dec_to_bin(dec_number,):
    if dec_number == 0:
        return 0
    if dec_number % 2 == 0:
        return 0 + 10 * dec_to_bin(dec_number // 2)
    else:
        return 1 + 10 * dec_to_bin(dec_number // 2)


f = lambda dec_number: 0 if dec_number == 0 else f(dec_number // 2) * 10 + (0 if dec_number % 2 == 0 else 1)  # just a way to solve

print(dec_to_bin(98))
print(f(98))