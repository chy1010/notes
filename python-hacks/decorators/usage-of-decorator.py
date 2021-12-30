"""
may refer: https://github.com/milaan9/07_Python_Advanced_Topics/blob/main/004_Python_Decorators.ipynb
"""


def make_pretty(func):
    def inner():
        print("-- I got decorated!! --")
        func()

    return inner


def ordinary():
    print("I am ordinary")


@make_pretty
def pretty_ordinary():
    print("I am ordinary")


# this is equiv. to:
# pretty_orindary = make_pretty(pretty_orindary)

if __name__ == '__main__':

    ordinary()
    pretty_ordinary()

    pretty = make_pretty(ordinary)
    pretty()
