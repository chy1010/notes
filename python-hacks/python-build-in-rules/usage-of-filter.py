import numpy as np
from common import is_prime


def main():
    numbers = np.random.randint(2, int(1e6), size=20).tolist()
    prime_numbers = filter(is_prime, numbers)
    print('Selected numbers:')
    print(sorted(numbers))
    print('Prime numbers in the selected numbers:')
    print(list(prime_numbers))

if __name__ == '__main__':
    main()