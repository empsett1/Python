# Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие максимальное количество элементов.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# Порядок элементов менять нельзя

# dynamic programming with memoization: runtime O(n^2), memory using: O(n)
from math import ceil


def dyn_prog(elements: list) -> list:
    dp = [0] * (len(elements) + 1)  # memoization
    best_indexes = [0] * (len(elements) + 1)  # best indexes list

    def rec_seeker(index: int) -> int:
        # border case:
        if index == -1:
            return 0

        #recurrent relation
        if index == len(elements) or dp[index] == 0:
            max_length = 0
            best_ind = -1
            for inner_index in range(index):
                if index == len(elements) or elements[inner_index] < elements[index]:
                    rec_sec_val = rec_seeker(inner_index) + 1
                    if max_length < rec_sec_val:
                        max_length = rec_sec_val
                        best_ind = inner_index

            # here we save the new calculated values of dp and best index
            dp[index] = max_length
            best_indexes[index] = best_ind

        return dp[index]

    rec_seeker(len(elements))

    # back motion to capture the right numbers
    result = []  # resulting LIS
    ind = len(elements)
    while True:
        ind = best_indexes[ind]  # the best way's steps -> here we get the longest increasing subsequence char by char
        if ind != -1:
            result.insert(0, str(elements[ind]))
        else:
            break

    return result


print(dyn_prog([1, 5, 2, 3, 4, 6, 1, 7]))
print(dyn_prog([5, 2, 3, 4, 6, 1, 7]))
print(dyn_prog([1, 1, 1, 1, 1, 5, 2, 1, 3, 4, 6, 1, 2, 2, 7]))