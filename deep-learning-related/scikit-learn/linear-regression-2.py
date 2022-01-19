import numpy as np

def simple_linear_regression(raw_x, raw_y):
    n = np.size(raw_x)
    x = np.array(raw_x)
    y = np.array(raw_y)
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    num1 = np.sum(y*x) - n*y_mean*x_mean
    num2 = np.sum(x*x) - n*x_mean*x_mean
     
    b_1 = num1 / num2
    b_0 = y_mean - b_1 * x_mean
    
    return (b_0, b_1)

if __name__ == '__main__':
    
    x = [3, 6, 5, 7, 4, 5]
    y = [2, 10, 4, 6, 8, 6]
    
    print(simple_linear_regression(x,y))