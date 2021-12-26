from time import time
from functools import wraps
import random


def record_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'{func.__name__}: {time() - start} seconds.')
        return result

    return wrapper


@record_time
def is_prime(input: int) -> bool:
    if input % 2 == 0:
        return False
    counter = 3
    while counter**2 < input:
        if input % counter == 0:
            return False
        counter += 2
    return True


if __name__ == '__main__':

    N = random.randint(2, int(1e8))
    if is_prime(N):
        print(f'{N} is a prime.')
    else:
        print(f'{N} is not a prime.')
