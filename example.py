from typing import Union


def add(a: Union[int, float], b) -> Union[int, float]:

    return a + b


with open('example.txt', 'r') as file:
    content = file.read()
    print(content)


with open('example.txt', 'w') as file:
    file.write('Hello, world!')
