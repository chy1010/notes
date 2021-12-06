import numpy as np


def main():
    
    print(f'1-dimensional linear interpolation.')
    print(f'-'*50)

    xp = [1,2,3]
    fp = [3,2,0]

    for x, y in zip(xp, fp):
        print(f"{y} = f({x})")

    print(f'-'*50)

    print(f'interpolation result:')
    y = np.interp(2.5, xp, fp)
    print(f"{y} = f({2.5})")



if __name__ == '__main__':
    main()