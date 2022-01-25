
first_ten_prime_list = [2,3,5,7,11,13,17,19,23,29]

second_first_ten_prime_list = [p for p in first_ten_prime_list]
first_ten_prime_generator = (p for p in first_ten_prime_list)

if __name__ == '__main__':
    
    print(first_ten_prime_list)
    print(second_first_ten_prime_list)
    print(first_ten_prime_generator)
    
    for i in second_first_ten_prime_list:
        print(i, end=', ')
    
    print('')
    for i in first_ten_prime_generator:
        print(i, end=', ')
        
    print('')
    print(f'second_first_ten_prime_list is a {type(second_first_ten_prime_list)}.')
    print(f'first_ten_prime_generator is a {type(first_ten_prime_generator)}.')