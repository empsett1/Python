from functools import reduce


def rle_encoding(file_path: str) -> None:
    with open(file_path, "r") as file:
        str_list = file.readlines()
        general_str = reduce(lambda x, y: x + y, str_list)
        result_str = ''

        index = 0
        while index < len(general_str):
            print(f'index: {index}, len = {len(general_str)}')
            consecutive_identical_symbols_counter = 1
            while index < len(general_str) - 1 and general_str[index] == general_str[index + 1]:

                consecutive_identical_symbols_counter += 1
                index += 1

            result_str += f'{general_str[index]}{consecutive_identical_symbols_counter}'
            index += 1

    with open("result_enc.txt", "w") as file:
        print(result_str)
        file.write(result_str)


def rle_decoding(file_path: str) -> None:
    with open(file_path, "r") as file:
        str_list = file.readlines()
        general_str = reduce(lambda x, y: x + y, str_list)

        result_str = ''

        index = 0
        while index < len(general_str):
            print(f'index: {index}, len = {len(general_str)}')
            curr_char = general_str[index]
            index += 1
            curr_number = 0
            while index < len(general_str) and general_str[index].isdigit():
                curr_number += int(general_str[index])
                index += 1
            print(curr_number)
            result_str += curr_char * curr_number

    with open("result_dec.txt", "w") as file:
        print(result_str)
        file.write(result_str)


rle_encoding('text.txt')

rle_decoding('encoded.txt')