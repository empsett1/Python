# Создать и заполнить файл случайными целыми значениями.
# Выполнить сортировку содержимого файла по возрастанию.

import random
import time
from functools import reduce


def fill_in_random(quantity: int, abs_val: int):
    with open("number_4_task.txt", "w") as file:
        for i in range(random.randint(1, quantity)):
            file.write(str(random.randint(-abs_val, abs_val)) + '\n')


def sort():
    with open("number_4_task.txt", "r") as file:
        numbers_list_int = [int(x) for x in file.readlines()]
        print(f'initial numbers to be sorted: {numbers_list_int}')
        sorted_ints = sorted(numbers_list_int)
        print(f'sorted ones: {sorted_ints}')
    with open("number_4_task.txt", "w") as file:
        for num in sorted_ints:
            file.write(str(num) + '\n')


fill_in_random(25, 100)

sort()