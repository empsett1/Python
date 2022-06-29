# 1. Напишите программу, удаляющую из текста все слова содержащие "абв". Используйте знания с последней лекции. Выполните ее в виде функции.
# -*- coding: utf-8 -*-
from functools import reduce


def delete_char_sequence(text: list[str]) -> list:
    return list(filter(lambda x: x.lower().find('абв') == -1, text))


print(delete_char_sequence(['лалалабвло', 'фбтатамв', 'абабавв']))


text = 'абв сидели на трубе. а упала, б пропала, кто остался на трубе, если были абв и бебебе. ' \
       'очень долго абв шел по старой тропе. долго ли, коротко ли блуждал он во мраке, но встретился ему абвев - тот еще ходок.' \
       'абвев встретил старого друга абв и ушел прочь с дороги его, потому что не нравился ему абв'
test1 = 'абвал,'


signs = [',', '.', ':', ';', '!', '?', '-', '"', '(', ')']


# working on the text given
def filter_text(text_in: str):
    parts = text.split(' ')
    print(parts)

    new_parts = []

    for part in parts:
        flag = True

        new_part = part

        if len(part) >= 2 and part[0] == '(' and part[1] == '"':
            new_parts.append(part[:-(len(part) - 2)])
            new_part = part[-(len(part) - 2):]
        elif len(part) >= 1 and (part[0] == '(' or part[0] == '"'):
            new_parts.append(part[:-(len(part) - 1)])
            new_part = part[-(len(part) - 1):]

        for index_of_character in range(len(new_part)):
            if new_part[index_of_character] in signs:
                new_parts.append(new_part[:-(len(new_part) - index_of_character)])
                new_parts.append(new_part[-(len(new_part) - index_of_character):])
                flag = False
                break
        if flag:
            new_parts.append(new_part)

    print(new_parts)

    result_parts = delete_char_sequence(new_parts)

    return reduce(lambda x, y: x + y + ' ', result_parts, '')


print(f'result text: {filter_text(text)}')
print([1, 2, 3, 4, 5, 6, 7][-2:])
print([1, 2, 3, 4, 5, 6, 7][:-2])
