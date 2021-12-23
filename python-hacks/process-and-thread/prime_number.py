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
        counter = 2 
        while counter * counter < self.number: 
            if self.number % counter == 0:
                print(f'{self.number:-8d} is not a prime number: {self.number:-8d} = {counter}*{self.number // counter}') 
                return 
            counter += 1 
        print(f'{self.number:-8d} is a prime number.')

if __name__ == '__main__':
    threads = [] 
    inputs = np.random.randint(low=2, high=int(1e8), size=10).tolist()
    for input in inputs:
        thread = PrimeNumber(input) 
        threads += [thread] 
        thread.start() 
    
    for x in threads: 
        x.join()
