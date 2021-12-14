# hash of an object comes from the address
import random
from copy import deepcopy


class Frame:
    def __init__(self, dataset, name):
        self.dataset = dataset
        self.name = name

    def __str__(self):
        return f'{self.dataset}/{self.name}'

    def __repr__(self):
        return f'{self.dataset}/{self.name}'

    def __hash__(self):
        return hash((self.dataset, self.name))

    def __eq__(self, another):
        return isinstance(another, Frame) and hash(self) == hash(another)


if __name__ == '__main__':

    frame_list = [Frame('mydataset', f'{i:03d}.jpg') for i in range(10)]

    refer_frame = random.choice(frame_list)
    target_frame = random.choice(frame_list)

    print('the hash code of the two frames:')
    print(hash(refer_frame), hash(target_frame))

    refer_frame = frame_list[0]
    target_frame = deepcopy(frame_list[0])
    print('the hash code of the a single frame:')
    print(hash(refer_frame), hash(target_frame))

    print('-=-' * 30)
    print('the equal of two frames?')
    print(refer_frame == target_frame)

    print('-=-' * 30)

    print(refer_frame)