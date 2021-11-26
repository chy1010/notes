"""[summary]
    shlex -- simple lexcial analysis

"""
import shlex

# use shlex.shlex() to separate contents with quotation marks ' & "

with open('python-hacks/test-file/shlex-example.txt', mode='r') as fp:
    text = fp.read()

rets = shlex.shlex(text)
print(f'The return of shlex.shlex() is an iterable object: {type(rets)}')
print('It consists of the separated contents:')
print('-' * 30)
for ret in rets:
    print(ret)