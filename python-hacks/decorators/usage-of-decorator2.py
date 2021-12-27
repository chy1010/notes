"""
may refer: https://github.com/milaan9/07_Python_Advanced_Topics/blob/main/004_Python_Decorators.ipynb
"""

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def greeting():
    return 'Welcome to Python'

if __name__ == '__main__':
    print(greeting())   # WELCOME TO PYTHON