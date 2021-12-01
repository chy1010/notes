"""[summary]
    Usage of nn.Conv2d() and nn.ConvTranspose2d()
"""
import torch
from torch import nn
import numpy as np
from copy import copy

# image
image = np.arange(64).reshape(8,8)
image = image[np.newaxis, np.newaxis, ...]
tensor = torch.Tensor(image)

print(f'The input tensor of shape {tensor.shape}: \n{tensor}')

conv = nn.Conv2d(1, 1, kernel_size=3, stride=2, padding=1, bias=False)

# fill conv's weight by 1
conv.weight.data.fill_(1)
# if bias: conv.bias.data.fill_(1)

x = copy(tensor)


x = conv(x)
print(x.shape)
print('-=-'*30)
print(x)
print('-=-'*30)

deconv = nn.ConvTranspose2d(1, 1, kernel_size=3, stride=2, padding=1, output_padding=1, bias=False)
deconv.weight.data.fill_(1)

x = deconv(x)
print(x.shape)
print('-=-'*30)
print(x)
print('-=-'*30)

