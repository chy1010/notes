"""
several examples of using map
"""
from time import time


def main():
    # convert list of number strings to numbers

    numbers_str = ['1', '2', '3', '4', '5']  # iterable
    numbers_int = map(int, numbers_str)

    print(type(numbers_int))
    print(f'is iterable?: {hasattr(numbers_int, "__iter__")}')

    print(next(iter(numbers_int)))
    print(list(numbers_int))  # [1, 2, 3, 4, 5]

    # uppercase
    names = ['Alice', 'Bob', 'Candy', 'David', 'Eddie']

    start_time = time()
    N = 10000
    for _ in range(N):
        names_upper_cased = map(lambda name: name.upper(), names)
    print(f'duration of {N} times of mapping: {time() - start_time}')
    print(list(names_upper_cased))

    for _ in range(N):
        names_upper_cased = [name.upper() for name in names]
    print(
        f'duration of {N} times of list comprehension: {time() - start_time}')
    print(list(names_upper_cased))


if __name__ == '__main__':
    main()