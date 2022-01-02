"""
usage of counter in collections
"""
from collections import Counter

def main():
    string = 'aabbbcdererere'
    counter = Counter(string)
    print(counter)


if __name__ == '__main__':
    main()