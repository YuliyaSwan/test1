from typing import List


def get_same_numbers(list_1: List[int], list_2: List[int]) -> List[int]:
    """Функция для получения одинаковых чисел"""
    new_list = list()
    for i in list_1:
        if i in list_2:
            new_list.append(i)

    return new_list


if __name__ == "__main__":
    print(get_same_numbers([1, 2, 3, 4], [3, 4, 5, 6]))
