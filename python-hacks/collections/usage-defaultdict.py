from collections import defaultdict

# may refer: https://realpython.com/python-defaultdict/


# https://stackoverflow.com/questions/30354674/how-to-use-a-defaultdict-with-a-lambda-expression-to-make-the-default-changeable

# class MyDefaultDict(defaultdict):
#     def __init__(self, func):
#         super(self.__class__, self).__init__(self._func)
#         self.func = func

#     def _func(self):
#         return self.func(self.cur_key)
        
#     def __getitem__(self, key):
#         self.cur_key = key
#         return super().__getitem__(self.cur_key)

def main():
    s = 'mississippi'
    d = defaultdict(int)
    for k in s:
        d[k] += 1
    print(d)

    s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
    d = defaultdict(set)
    for k, v in s:
        d[k].add(v)
    print(d)

    d1 = dict()
    d2 = defaultdict(list)
    # print(d1['a'])
    # KeyError: 'a'
    print(d2['a'])

    c = defaultdict(lambda: 3)
    s = 'mississippi'
    for k in s:
        if k == 's':
            c[k] = 5566
        else:
            c[k]

    print(c)

    
    baseLevel = 0
    food = defaultdict(lambda: baseLevel)
    print(food['banana'])

    baseLevel += 10
    print(food['apple'])

    print(food['banana'])


if __name__ == '__main__':
    main()