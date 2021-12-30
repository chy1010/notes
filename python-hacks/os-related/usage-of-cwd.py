import os
from pathlib import Path

if __name__ == '__main__':

    cwd = os.getcwd()

    file_folder = Path(__file__).parent
    os.chdir(file_folder)
    print(f'current working folder: {os.getcwd()}')

    os.chdir(cwd)
    print(f'current working folder: {os.getcwd()}')