
def first_ten_primes():
    prime_list = [2,3,5,7,11,13,17,19,23,29]
    for i in prime_list:
        yield i



if __name__ == '__main__':
    
    for prime in first_ten_primes():
        print(prime, end=', ')

    print('')
    print(f'the function first_ten_primes() is of type {type(first_ten_primes())}.')