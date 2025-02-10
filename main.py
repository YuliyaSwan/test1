def list_of_numbers(my_list):
    avg = sum(my_list) / len(my_list)
    new_list = []
    for i in my_list:
        if i < avg:
            new_list.append(i)

    return new_list


print(list_of_numbers([1, 2, 3, 4, 5]))


def list_of_lines(my_list):
    total_list = []
    for i in my_list:
        if i not in total_list:
            total_list.append(i)
        else:
            pass

    return total_list


print(list_of_lines(['apple', 'banana', 'orange', 'apple']))


from src.masks import split_string


if __name__ == '__main__':
    print(split_string('sevennn'))
