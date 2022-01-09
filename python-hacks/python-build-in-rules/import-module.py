from importlib import import_module

np = import_module('numpy')
print(np.__version__)