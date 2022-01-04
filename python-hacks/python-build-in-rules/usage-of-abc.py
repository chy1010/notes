"""
https://docs.python.org/3.5/library/abc.html
class abc.ABCMeta
    Metaclass for defining Abstract Base Classes (ABCs)
"""
from abc import ABCMeta

class MyABC(metaclass=ABCMeta):
    pass

if __name__ == '__main__':

    # Register subclass as a “virtual subclass” of this ABC
    MyABC.register(tuple)
    assert issubclass(tuple, MyABC)
    assert isinstance((), MyABC)


