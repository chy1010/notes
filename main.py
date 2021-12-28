"""
This is aim to execute the program in toplevel and to import functions in the `common` folder.

Now only allow in this form: `python main.py path-to-program.py`,
and the functions in `common` need to be imported in the form `from common import ...`
"""

import sys
import importlib  

if __name__ == '__main__':

    test_mod = sys.argv[1]
    test_mod = test_mod.split('.')[0]
    test_mod = test_mod.replace('/', '.')

    test_mod = importlib.import_module(test_mod)
    test_mod.main()