

class PrimeNumbers:

    def __init__(self, max=100):
        self.max = max
        self.prime_list = [2,3,5]

    def __iter__(self):
        self.n = 0
        self.p = 6
        return self

    def __next__(self):
        if self.n > self.max:
            raise StopIteration
        if self.n < len(self.prime_list):
            self.n += 1
            return self.prime_list[self.n-1]
        else:
            is_prime = False
            for j in range(self.p, self.max):
                if not self.divide_by_list(j):
                    is_prime = True
                    break
            self.p = j+1
            if is_prime:
                self.prime_list.append(j)
            else:
                raise StopIteration
        self.n += 1
        return j
            
    def divide_by_list(self, p):
        return any([ p % prime == 0 for prime in self.prime_list if (prime ** 2 <= p)])


if __name__ == '__main__':
    
    number = 1000
    prime_less_than_number = PrimeNumbers(max=number)
    
    for prime in prime_less_than_number:
        print(prime, end=', ')