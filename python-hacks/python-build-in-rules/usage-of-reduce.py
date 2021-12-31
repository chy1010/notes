"""
reduce: apply a function on an iterable object in
the following sense,
    reduce(f, [x1, x2, x3]) = f(f(x1, x2), x3)
Notice that the function must be a binary operation.

refer: https://www.liaoxuefeng.com/wiki/1016959663602400/1017329367486080
"""
from functools import reduce

def fn(x,y):
    return 10*x+y

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2int(s: str):
    assert s in DIGITS, f'{s} is not a digit.'
    return DIGITS[s]

def main():
    num = reduce(fn, map(char2int, '3345678'))
    print(num)

if __name__ == '__main__':
    main()
