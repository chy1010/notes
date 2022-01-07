import numpy as np

A = np.arange(48).reshape(4,4,3)

attrs = ['ndim', 'shape', 'size', 'dtype', 'itemsize']

for attr in attrs:
    print(f'{attr}: ', getattr(A, attr))

print(f'shape: {A.shape}')
print(A.strides)
A = A.reshape(4,4,3)
print(f'shape: {A.shape}')
print(A.strides)
print(A.data.contiguous)
print(A.data.c_contiguous)
print(A.data.f_contiguous)

A = np.ascontiguousarray(A)