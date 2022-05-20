# Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

def get_sequence(length):
    list = []
    pow = 1

    for i in range(0, length):
        list.append(pow)
        pow *= -3

    return list

# Пользователь вводит две строки, определить количество вхождений одной строки s2 в другую s1

def count_inclusive_substrings(s1, s2):
    counter = 0
    i = -1
    while True:
        i = s1.find(s2, i + 1)
        if i == -1:
            return counter
        counter += 1


# Сформировать программу, получающую набор произведений чисел от 1 до N. Для N = 4: [1, 2, 6, 24]

def get_product_list(N):
    elements = []
    curr_fact = 1

    for i in range(1, N + 1):
        curr_fact *= i
        elements.append(curr_fact)

    return elements


# Посчитать сумму цифр в вещественном числе

def get_sum(number):
    while (number % 1 != 0):
        number *= 10

    sum = 0

    while (number > 0):
        sum += number % 10
        number //= 10

    return sum


print(count_inclusive_substrings('aaaaaashaaaashaaaaaashaaaa', 'asha')) # an example for 1st task

print(get_sequence(6))  # an example for 2nd task

print(get_product_list(5))  # an example for 3rd task

print(get_sum(888.88))  # an example for 4th task