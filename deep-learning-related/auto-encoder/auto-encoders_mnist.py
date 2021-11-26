"""[summary]
X: sample space, Z: feature space.
g: X -> Z is an encoder.
f: Z -> X is a decoder.

x: sample -> z: feature -> x_hat: reconstruct sample
x -> z = g(x) -> x_hat = f(z) = f(g(x))

Auto-encoder: aim to find g, f to minimize sum of ||x - x_hat||.
"""

import numpy as np
import torch
from torch import nn
from torchvision import datasets, transforms


class SimpleANNAutoEncoder(nn.Module):
    def __init__(self,
                 sample_dim: int = 784,
                 feature_dim: int = 4,
                 num_classes: int = 10):
        super().__init__()
        self.encoder_layer = nn.Linear(sample_dim, feature_dim)
        self.encoder_relu = nn.ReLU()
        self.decoder_layer = nn.Linear(feature_dim, sample_dim)
        self.decoder_relu = nn.ReLU()
        self.classifier = nn.Linear(feature_dim, num_classes)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        feat = self.encoder_relu(self.encoder_layer(x.flatten(start_dim=1)))
        prediction = self.softmax(self.classifier(feat))
        recovered_x = self.decoder_relu(self.decoder_layer(feat))
        return recovered_x, prediction


if __name__ == '__main__':

    transform = transforms.Compose([transforms.ToTensor()])

    train_dataset = datasets.MNIST(root='~/.cache/torch/data/',
                                   download=True,
                                   train=True,
                                   transform=transform)
    train_dataloader = torch.utils.data.DataLoader(dataset=train_dataset,
                                                   batch_size=64,
                                                   shuffle=True)

    test_dataset = datasets.MNIST(root='~/.cache/torch/data/',
                                  download=True,
                                  train=False,
                                  transform=transform)
    test_dataloader = torch.utils.data.DataLoader(dataset=test_dataset,
                                                  shuffle=True)

    model = SimpleANNAutoEncoder(sample_dim=784, feature_dim=4, num_classes=10)
    class_loss = nn.CrossEntropyLoss()
    recover_loss = nn.L1Loss()

    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
    num_epoch = 50

    model.train()
    num_train_data = len(train_dataset)

    for epoch in range(num_epoch):
        total_loss = 0.0
        correct = 0
        recovered_correct = 0
        batch_size = len(next(iter(train_dataloader))[0])
        for data in train_dataloader:
            X_train, y_train = data
            X_train = X_train.float()

            X_hat, output = model(X_train)
            pred = output.clone().detach()
            pred = torch.argmax(pred, dim=-1)
            correct += torch.sum(pred == y_train.data)

            optimizer.zero_grad()

            # only MSE_loss need to do one-hot encoding:
            # y_train = F.one_hot(y_train, 10).float()

            loss_cla = class_loss(output, y_train)
            loss_rec = recover_loss(X_train.flatten(start_dim=1), X_hat)
            loss = loss_cla + loss_rec
            # loss.requires_grad_(True)
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * batch_size

            recovered_correct += np.sum(
                torch.abs((X_train.flatten(start_dim=1) -
                           X_hat).detach()).numpy() < 0.5)

        print(
            f'[Epoch {epoch+1:03d}] loss: {total_loss: 9.4f};',
            f'acc.: {100*correct/num_train_data:5.2f}%;',
            f'recover rate: {100*recovered_correct/784/num_train_data:5.2f}%.')

    # model.eval()
    # test_data = next(iter(test_dataloader))
    # X, label = test_data
    # X_in = X.float()
    # recovered_X, prediciton = model(X_in)

    # img_X = (255 * X.numpy()).astype(np.uint8).reshape(28,28,1)
    # rec_X = recovered_X.detach().numpy() * 255
    # rec_X = rec_X.astype(np.uint8).reshape(28,28,1)

    # import cv2
    # cv2.imwrite('temp/X.png', img_X)
    # cv2.imwrite('temp/rec_X.png', rec_X)