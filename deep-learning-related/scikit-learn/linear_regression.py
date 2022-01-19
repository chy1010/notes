import numpy as np
from sklearn.linear_model import LinearRegression


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
    data = [(1.1, 39343.0), (1.3, 46205.0), (1.5, 37731.0), (2.0, 43525.0), (2.2, 39891.0), (2.9, 56642.0), (3.0, 60150.0), (3.2, 54445.0), (3.2, 64445.0), (3.7, 57189.0)]

    year_exps = [year_exp for (year_exp, salary) in data]
    salaries = [salary for (year_exp, salary) in data]
    print(f"working exp: {year_exps}")
    print(f"salaries: {salaries}")

    # usual linear regression is done by the least square method.
    linear_regression = LinearRegression()
    # model fitting (scikit-learn)
    linear_regression.fit(np.array(year_exps, dtype=np.float16)[:, None],
                          np.array(salaries, dtype=np.float16))
    # create regression curve / prediction curve
    xp = np.arange(1.0, 4.0, 0.1)
    y = linear_regression.predict(xp[:, None])

    print(f"y = {linear_regression.coef_.item()} * xp + {linear_regression.intercept_}")

    # plt.scatter(year_exps, salaries);
    # plt.plot(xp, y, color = 'r');
    # plt.xlabel('working experience (year)');
    # plt.ylabel('annual salary (USD)');
    
    
    b_0, b_1 = simple_linear_regression(year_exps, salaries)
    yy = b_1 * xp + b_0
    print(f'y = {b_1} * xp + {b_0}')
    
    print(sum(abs(y-yy)))