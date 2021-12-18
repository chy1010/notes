import json
import argparse

import fileinput
import re
from pathlib import Path

import copy


def parse_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--file', type=str, default=None)
    parser.add_argument('--choose_parameter', type=str, default=None)
    parser.add_argument('--set_value', type=str, default=None)
    args = parser.parse_args()
    return args


def replace(filename, var, value):
    value = json.dumps(value)
    found = False
    for line in fileinput.input(filename, inplace=True):
        if var in line:
            if not found:
                found = True
                RHS = re.split('(=|:|,|\))', line)
                # RHS = [c.strip() for c in RHS]
                replaced = False
                for i, char in enumerate(RHS):
                    if char == ',':
                        RHS[i - 1] = value
                        replaced = True
                        break
                    if char == ')':
                        RHS[i - 1] = value
                        replaced = True
                        break
                if not replaced:
                    RHS[-1] = value
                line = "".join(RHS)
                if not replaced:
                    line += '\n'
            else:
                raise NameError(f'{var} ambigous')
        print(line, end="")
    if not found:
        raise NameError(f"{var} not found in {filename}")


def main():
    args = parse_args()
    test_file = args.file
    choose_parameter = args.choose_parameter
    value = args.set_value

    assert isinstance(choose_parameter, str) and isinstance(value, str)
    replace(test_file, choose_parameter, value)


if __name__ == '__main__':
    main()