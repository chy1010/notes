"""[summary]
    Usage of nn.Conv2d() and nn.ConvTranspose2d()

    - output_padding: If stride > 1, then the remainder of 
      `(H - kernel + 2*padding) % stride` may be in range(0, stride).
      Hence the output_padding is the remainder that helps recovering,
      i.e. x.shape == deconv(conv(x)).shape
"""
import torch
from torch import nn
import numpy as np
from copy import copy

# set parameters
N = 10
conv_params = dict(kernel_size=5, stride=3, padding=2, bias=False)
deconv_params = dict(kernel_size=5,
                     stride=3,
                     padding=2,
                     bias=False,
                     output_padding=0)

print('-=-' * 30)
print('Calculation of the input and output shapes of a conv layer.')

w_in = N
w_out = int(
    np.floor((w_in + 2 * conv_params['padding'] - conv_params['kernel_size']) /
             conv_params['stride']) + 1)
print(f'input size: {w_in}', f'expected output size: {w_out}')

print('-=-' * 30)
print('Calculation of the input and output shapes of a deconv layer.')
w_in = w_out
w_out = (w_in - 1) * deconv_params['stride'] - 2 * deconv_params[
    'padding'] + deconv_params['kernel_size'] + deconv_params['output_padding']
print(f'input size: {w_in}', f'expected output size: {w_out}')
print('-=-' * 30)

# setting of conv and deconv layers
conv = nn.Conv2d(1, 1, **conv_params)
# fill conv's weight by 1
# if bias: conv.bias.data.fill_(1)
conv.weight.data.fill_(1)
deconv = nn.ConvTranspose2d(1, 1, **deconv_params)
deconv.weight.data.fill_(1)

# image
image = np.arange(N**2).reshape(N, N)
image = image[np.newaxis, np.newaxis, ...]
tensor = torch.Tensor(image)

print(f'The input tensor of shape {tensor.shape}: \n{tensor}')

x = copy(tensor)
x = conv(x)

print('-==-' * 20)
print(x.shape)
print(x)
print('-==-' * 20)

x = deconv(x)

print('-==-' * 20)
print(x.shape)
print(x)
print('-=-' * 30)
