from functools import reduce

def is_prime(input: int) -> bool:
    if input % 2 == 0:
        return False
    counter = 3
    while counter**2 < input:
        if input % counter == 0:
            return False
        counter += 2
    return True

def str2int(s: str):
    DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def fn(x,y):
        return 10*x+y
    def char2digit(s: str):
        assert s in DIGITS, f'{s} is not a digit.'
        return DIGITS[s]
    return reduce(fn, map(char2digit, s))
