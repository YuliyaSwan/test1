def split_string(string: str):
    middle = len(string) // 2

    new_string = string[0:middle] + "--" + string[middle:]

    return new_string

