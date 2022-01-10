"""
to avoid access wrong memory
https://stackoverflow.com/questions/47483579/how-to-use-numpy-as-strided-from-np-stride-tricks-correctly
"""

import numpy as np
from numpy.lib.stride_tricks import as_strided
# numpy.lib.stride_tricks.as_strided(x, shape=None, strides=None, subok=False, writeable=True)

BASIC_STRIDE = dict(uint8=1, uint16=16, int16=2, int32=4, int64=8)
A = np.arange(16)

print(f'A is an ndarray of shape {A.shape}: {A}.')
print(f'The basic stride for the dtype {str(A.dtype)}: {BASIC_STRIDE[str(A.dtype)]}.')

print('--'*30)
B = A.reshape(4,4)
print('B = A.reshape(4,4)')
print(B)

print('--'*30)
print('Here use as_strided to do reshape:')

stride_size = BASIC_STRIDE[str(A.dtype)]
strides = (4 * stride_size, 1 * stride_size)
C = as_strided(A, shape=(4,4), strides=strides)
print(f'stride_size for {A.dtype}: {stride_size}')
print(f'The strides is {strides}.')
print(f'C = as_strided(A, shape=(4,4), strides={strides})')

print(C)

print('--'*30)
print('Now we handle to split overlapping patches.')
print('Decide to split to four 3-by-3 split images: of shape (2,2,3,3)')
shape = (2,2,3,3)
strides = [4,1,4,1]
strides = tuple(stride * stride_size for stride in strides)
C = as_strided(A, shape=shape, strides=strides)
print(C.shape)
print(C)

print('--'*30)
print('test to split 3 channel images')

A = np.arange(27).reshape(3,3,3)
print('R')
print(A[...,0])
print('G')
print(A[...,1])
print('B')
print(A[...,2])

shape = (2,2,2,2,3)
strides = [9, 3, 9, 3, 1]
strides = tuple(stride * stride_size for stride in strides)
C = as_strided(A, shape=shape, strides=strides)
print(C.shape)
print('R')
print(C[...,0])
print('G')
print(C[...,1])
print('B')
print(C[...,2])


print('--' * 30)
print('Try to split overlapping images:')
from itertools import product

IMAGE_WIDTH = 3840
IMAGE_HEIGHT = 2160
PATCH_WIDTH = 1120
PATCH_HEIGHT = 1120
STRIDES = 1088

array_strides = None

if isinstance(STRIDES, tuple):
    x_stride = STRIDES[0]
    y_stride = STRIDES[1]
else:
    assert isinstance(STRIDES, int)
    x_stride = y_stride = STRIDES
    
x_steps = int(np.ceil((IMAGE_WIDTH - PATCH_WIDTH) / x_stride))
y_steps = int(np.ceil((IMAGE_HEIGHT - PATCH_HEIGHT) / y_stride))

patch_coords = []
for num_x_step, num_y_step in product(range(x_steps+1), range(y_steps+1)):
    x1 = num_x_step * x_stride
    y1 = num_y_step * y_stride
    # if x1 + PATCH_WIDTH >= IMAGE_WIDTH:
    #     x1 = IMAGE_WIDTH - PATCH_WIDTH
    # if y1 + PATCH_HEIGHT >= IMAGE_HEIGHT:
    #     y1 = IMAGE_HEIGHT - PATCH_HEIGHT
    x2 = x1 + PATCH_WIDTH
    y2 = y1 + PATCH_HEIGHT
    
    patch_coords.append([x1, y1, x2, y2])    
print(patch_coords)

x_pixels_need_to_padding = (IMAGE_WIDTH - PATCH_WIDTH) % x_stride
y_pixels_need_to_padding = (IMAGE_HEIGHT - PATCH_HEIGHT) % y_stride
# padding: 114

image = np.random.randint(low=0, high=255, size=(IMAGE_HEIGHT, IMAGE_WIDTH, 3))

print(f'y_pixels_need_to_padding: {y_pixels_need_to_padding}')
print(f'x_pixels_need_to_padding: {x_pixels_need_to_padding}')
print(f'image height: {IMAGE_HEIGHT}')
print(f'image width: {IMAGE_WIDTH}')
n_pad = ((0, y_pixels_need_to_padding), (0, x_pixels_need_to_padding), (0,0))

image_1 = np.pad(image, pad_width=n_pad, mode='constant', constant_values=0)

FULL_PAD_WIDTH = IMAGE_WIDTH + x_pixels_need_to_padding
FULL_PAD_HEIGHT = IMAGE_HEIGHT + y_pixels_need_to_padding
# print(image.shape)
# print(image.data.contiguous)
# print(image_1.data.contiguous)

itemsize = image_1.itemsize
strides = [y_stride*FULL_PAD_WIDTH*3, x_stride*3, FULL_PAD_WIDTH*3, 3, 1]
strides = tuple([ stride * itemsize for stride in strides])

patches = as_strided(image_1, shape=(y_steps+1, x_steps+1, PATCH_HEIGHT, PATCH_WIDTH, 3),
                     strides=strides,
                     )

print(patches.shape)
