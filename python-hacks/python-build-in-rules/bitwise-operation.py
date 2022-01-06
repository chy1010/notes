import random

if __name__ == '__main__':
    
    x = random.randint(1, 1024)
    print(f'Convert integer {x} to binary format: bin(x) = {bin(x)}')
    
    print(f'[shift operation]')
    
    print(f'left shift by 1 bit: x<<1 = {x<<1}, {bin(x<<1)}')
    print(f'right shift by 1 bit: x>>1 = {x>>1}, {bin(x>>1)}')