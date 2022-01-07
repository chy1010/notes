import numpy as np

print('stride of different d-type:')

dtypes = ['uint8', 'uint16', 'int16', 'int32', 'int64', 'intc']

for dtype in dtypes:
    X = np.arange(16).astype(getattr(np, dtype))
    print(f'{str(X.dtype):6s}: {X.strides}')