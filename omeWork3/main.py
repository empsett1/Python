# Найти НОК двух чисел

def gcd(a: int, b: int):
    minimum = min(a, b)
    maximum = max(a, b)
    while True:
        rem = maximum % minimum
        if rem == 0:
            return minimum
        maximum = max(rem, minimum)
        minimum = min(rem, minimum)

def lcm(a: int, b: int):
    return a * b // gcd(a, b)


print(gcd(77, 121))
print(gcd(3, 5))
print(gcd(45, 60))

print(lcm(77, 121))
print(lcm(3, 5))
print(lcm(45, 60))

# print(lcm("", ""))

# Вычислить число  c заданной точностью d
# Пример: при d = 0.001,  c= 3.141.
from decimal import Decimal
from decimal import getcontext

getcontext().prec = 25

def chislo_pi(precision: float) -> float:
    pi = 3.0
    i = 2
    delta = 1
    while True:
        prev_delta = delta
        delta = (-1 if i % 4 == 0 else 1) * 4 / (i * (i + 1) * (i + 2))
        pi += delta
        k = abs(prev_delta - delta)
        print(f'i = {i}, pi = {pi}, current delta = {k}')
        if k < precision:
            return pi
        i += 2

print(chislo_pi(0.00000001))

# Составить список простых множителей натурального числа N

import math

def get_primes(n):  # Eratosthenes' sieve
    """
    :param n: max number to which we should build the primes list
    :return: list of primes before or equal to n
    """

    a = []
    for i in range(n + 1):
        a.append(i)
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1

    a = set(a)
    a.remove(0)
    return a


def deliteli(number: int):
    primes = get_primes(int(math.sqrt(number)))
    factorization_dictionary = {}
    for prime in primes:
        power_counter = 0
        while number % prime == 0:
            number //= prime
            power_counter += 1
        if power_counter >= 1:
            factorization_dictionary[prime] = power_counter
    if number > 1:
        factorization_dictionary[number] = 1
    return factorization_dictionary

print(deliteli(3*3*3*3*3*11*17*199))
print(deliteli(640320))
print(deliteli(6670))
print(deliteli(640320 // (32 * 3)))
print(deliteli(13717421))
print(deliteli(36758392918475747))

# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

list_of_elements = [1, 2, 3, 5, 1, 5, 3, 10]


def remove_repeat_items(elements):
    return set(elements)


print(remove_repeat_items(list_of_elements))