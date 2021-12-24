"""
refer: https://github.com/arifulhaqueuc/python-multithreading-examples
"""
import threading
import numpy as np


class PrimeNumber(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.number = number

    def run(self):
        if self.number % 2 == 0:
            print(f'{self.number:-8d} is not a prime number:',
                  f'{self.number:-8d} = 2*{self.number // 2}')
            return
        counter = 3
        while counter * counter < self.number:
            if self.number % counter == 0:
                print(
                    f'{self.number:-8d} is not a prime number:',
                    f'{self.number:-8d} = {counter}*{self.number // counter}')
                return
            counter += 2
        print(f'{self.number:-8d} is a prime number.')


if __name__ == '__main__':
    threads = []
    inputs = np.random.randint(low=2, high=int(1e8), size=10000).tolist()
    inputs = [6 * input + 1 for input in inputs]
    for input in inputs:
        thread = PrimeNumber(input)
        threads += [thread]
        thread.start()

    # for x in threads:
    #     x.join()

    print(f'Join: wait for all thread endding. Then continue.')
    print(f'If no join, this line may be printed before all threads end.')