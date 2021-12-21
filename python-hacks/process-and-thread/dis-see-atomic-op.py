"""
[reference] https://www.maxlist.xyz/2020/03/15/gil-thread-safe-atomic/#google_vignette
"""

import dis

this_is_list = []
that_is_list = []


def list_sort():
    this_is_list.sort()
    return 'ok'


def list_append():
    that_is_list.append('text')
    return 'okok'


if __name__ == '__main__':

    print('-' * 100)
    print('list sort')
    print('-' * 100)
    dis.dis(list_sort)
    print('-' * 100)
    print('list append')
    print('-' * 100)
    dis.dis(list_append)
    print('-' * 100)
