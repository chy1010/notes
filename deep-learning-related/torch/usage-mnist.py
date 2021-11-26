import torch
import numpy as np
from torchvision import datasets, transforms

import torch.nn as nn
import torch.nn.functional as F


class SimpleANN(nn.Module):
    """[summary]
    A simple artificial neural network:
        input_size -> (hidden layer) -> hidden_layer_size
                   -> (output_layer) -> output_size

    The values / signals are passed by `forward` function.
    The usage is like a call of the class.
    """
    def __init__(self, input_size=784, hidden_layer_size=1024, output_size=10):
        super(SimpleANN, self).__init__()
        self.first_layer = nn.Linear(input_size, hidden_layer_size)
        self.relu = nn.ReLU()
        self.second_layer = nn.Linear(hidden_layer_size, output_size)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        x = x.flatten(start_dim=1)
        x = self.first_layer(x)
        x = self.relu(x)
        out = self.second_layer(x)
        return out


if __name__ == '__main__':

    transform = transforms.Compose([transforms.ToTensor()])

    train_dataset = datasets.MNIST(root='~/.cache/torch/data/',
                                   download=True,
                                   train=True,
                                   transform=transform)
    train_dataloader = torch.utils.data.DataLoader(dataset=train_dataset,
                                                   batch_size=64,
                                                   shuffle=True)

    test_dataset = datasets.MNIST(root='~/.cache/torch/data/', download=True, train=False, transform=transform)
    test_dataloader = torch.utils.data.DataLoader(dataset=test_dataset, shuffle=True)

    # usage of sampler
    # train_dataset = datasets.MNIST(root='~/.cache/torch/data/', download=True, train=True, transform=transform)
    # indices = torch.randperm(len(train_dataset))[:5]
    # sampler = torch.utils.data.SubsetRandomSampler(indices, generator=None)
    # train_dataloader = torch.utils.data.DataLoader(dataset=train_dataset, sampler=sampler)

    # model_2 = SimpleANN(hidden_layer_size=1024)
    # loss_function_2 = nn.MSELoss()

    # # SGD: stochastic gradient descent
    # optimizer_2 = torch.optim.SGD(model_2.parameters(), lr=0.001)
    # num_epoch = 1000

    model = SimpleANN(28 * 28, 1024, 10)
    # loss_function = nn.MSELoss(reduction='mean')
    loss_function = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
    num_epoch = 10

    model.train()
    num_train_data = len(train_dataset)
    for epoch in range(num_epoch):
        total_loss = 0.0
        correct = 0
        batch_size = len(next(iter(train_dataloader))[0])
        for data in train_dataloader:
            X_train, y_train = data
            X_train = X_train.float()

            output = model(X_train)
            pred = output.clone().detach()
            pred = torch.argmax(pred, dim=-1)
            correct += torch.sum(pred == y_train.data)

            optimizer.zero_grad()

            # only MSE_loss need to do one-hot encoding:
            # y_train = F.one_hot(y_train, 10).float()

            loss = loss_function(output, y_train)
            # loss.requires_grad_(True)
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * batch_size

        print(
            f'[Epoch {epoch+1:03d}] total_train_loss: {total_loss: 9.4f}; training accuracy: {100*correct/num_train_data:5.2f}%'
        )


    model.eval()
    test_data = next(iter(test_dataloader))[0]
    X, label = test_data
    X_in = X.float() / 255
    recovered_X, prediciton = model(X_in)
    rec_X = recovered_X.numpy() * 255
    rec_X = rec_X.astype(np.uint8)

    import cv2
    cv2.imwrite('temp/X.png', X.numpy())
    cv2.imwrite('temp/rec_X.png', rec_X)
