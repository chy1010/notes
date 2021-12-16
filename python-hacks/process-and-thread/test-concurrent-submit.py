from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from time import time


def fibonacci(n):
    if n < 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':

    with ProcessPoolExecutor() as executor:
        result1 = executor.submit(fibonacci, 10)
        result2 = executor.submit(fibonacci, 20)

    print(f'f(10) = {result1.result()}')
    print(f'f(20) = {result2.result()}')

    print('= Test multi-thread / multi-process =')
    N = 5000

    start = time()
    for _ in range(N):
        fibonacci(20)
    print(
        f'Calculate fibonacci n = 20 for {N} times, takes time: {time() - start}'
    )

    start = time()
    with ProcessPoolExecutor() as executor:
        for _ in range(N):
            result = executor.submit(fibonacci, 20)
    print(
        f'Calculate fibonacci n = 20 for {N} times by using ProcessPoolExecutor(), takes time: {time() - start}'
    )

    start = time()
    with ThreadPoolExecutor() as executor:
        for _ in range(N):
            result = executor.submit(fibonacci, 20)
    print(
        f'Calculate fibonacci n = 20 for {N} times by using ThreadPoolExecutor(), takes time: {time() - start}'
    )
