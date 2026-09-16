import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

def task11():
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    y = np.array([0.1, 0.4, 0.1, 0.5, 0.4, 1, 2, 4, 3, 4, 3, 7, 2])

    A = np.vstack([x, np.ones(len(x))]).T

    m, c = np.linalg.lstsq(A, y, rcond=None)[0]
    print(m, c)
    plt.plot(x, y, 'o', label='Original', markersize=10)
    plt.plot(x, m*x, 'r', label='Linear extrapolation')
    plt.legend()
    plt.show()

def task12():
    rand = np.random.rand
    delta = 1.0
    x = np.linspace(-12, 21, 20)
    y = x ** 2 + delta * (rand(20) - 0.5)
    x += delta * (rand(20) - 2)

    print(x)
    print(y)

    m = np.vstack((x**2, x, np.ones(len(x)))).T
    s = np.linalg.lstsq(m, y, rcond=None)[0]
    x_prec = np.linspace(-14, 21, 101)
    plt.plot(x, y, 'D')
    plt.plot(x_prec, s[0] * x_prec**2 + s[1] * x_prec + s[2], '-', lw=2)
    plt.grid()
    plt.show()

    return x, y

def task13():
    x, y = task12()

    m = np.vstack((x**3, x**2, x, np.ones(len(x)))).T
    s = np.linalg.lstsq(m, y, rcond=None)[0]

    x_prec = np.linspace(-14, 21, 101)
    plt.plot(x, y, 'D')
    plt.plot(x_prec, s[0] * x_prec**3 + s[1] * x_prec**2 + s[2] * x_prec + s[3], '-', lw=2)
    plt.grid()
    plt.show()

def f1(x, b0, b1, b2):
    return b0 + b1 * np.exp(-b2 * x**2)

def f2(x, b0, b1):
    return b0 + b1 * x

def f3(x, b0, b1, b2):
    return b0 + b1 * x + b2 * x**2

def f4(x, b0, b1):
    return b0 + b1 * np.log(x)

def f5(x, b0, b1):
    return b0 * x ** b1

def calculationsAndFunction(f, beta, xdata):
    y = f(xdata, *beta)
    ydata = y + 0.5 * np.random.rand(len(xdata))
    beta_opt, beta_cov = sp.optimize.curve_fit(f, xdata, ydata)
    print(beta_opt)

    lin_dev = sum(beta_cov[0])
    print(lin_dev)

    residuals = ydata - f(xdata, *beta_opt)
    fres = sum(residuals ** 2)
    print(fres)

    fix, ax = plt.subplots()
    ax.scatter(xdata, ydata)
    ax.plot(xdata, y, 'r', lw=2)
    ax.plot(xdata, f(xdata, *beta_opt), 'b', lw=2)
    ax.set_xlim(1, 12)
    ax.set_xlabel(r"$x$", fontsize=18)
    ax.set_ylabel(r"$f(x, \beta)$", fontsize=18)
    plt.show()


def task2():
    beta1 = (0.25, 0.75, 0.5)
    beta2 = (0.25, 0.75)
    beta3 = (1, 2)

    xdata = np.linspace(1, 12, 100)
    calculationsAndFunction(f1, beta1, xdata)
    calculationsAndFunction(f2, beta2, xdata)
    calculationsAndFunction(f3, beta1, xdata)
    calculationsAndFunction(f4, beta3, xdata)
    calculationsAndFunction(f5, beta3, xdata)

def task3():
    url = 'https://raw.githubusercontent.com/AnnaShestova/salary-years-simple-linear-regression/master/Salary_Data.csv'
    data_frame = pd.read_csv(url)
    print(data_frame.to_string())
    X = data_frame.iloc[:, :-1].values
    y = data_frame.iloc[:, 1].values
    print(X)
    print(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    print(regressor.coef_)
    print(regressor.intercept_)
    y_pred = regressor.predict(X_test)
    df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    df.plot(kind='bar')
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()
    plt.scatter(X_test, y_test, color='gray')
    plt.plot(X_test, y_pred, color='red', linewidth=2)
    plt.show()

def task4():
    url = 'https://raw.githubusercontent.com/likarajo/petrol_consumption/master/data/petrol_consumption.csv'
    data_frame = pd.read_csv(url)
    print(data_frame.to_string())
    X = data_frame[['Petrol_tax', 'Average_income', 'Paved_Highways', 'Population_Driver_licence(%)']]
    y = data_frame['Petrol_Consumption']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)
    coeff_df = pd.DataFrame(regressor.coef_, X.columns, columns=['Coefficient'])
    print(coeff_df.to_string())
    Y_pred = regressor.predict(X_test)
    df = pd.DataFrame({'Actual': y_test, 'Predicted': Y_pred})
    print(df.to_string())
    print('Mean Squared Error: ', metrics.mean_squared_error(y_test, Y_pred))

def task5():
    x = np.array([1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
    y = np.array([2.0, 6.0, 4.0, 4.0, 2.0, 5.0])
    N = x.size
    A1 = np.vstack([x, np.ones(len(x))]).T

    m1, c1 = np.linalg.lstsq(A1, y, rcond=None)[0]
    print(m1, c1)

    y_lin = m1 * x + c1
    res_lin = y - y_lin
    SSE_lin = np.sum(res_lin**2)
    MSE_lin = SSE_lin / N
    sigma_lin = np.sqrt(SSE_lin / (N - 2)) if N > 2 else float('nan')

    print(f'MSE = {MSE_lin:.6f}')
    print(f'СКО = {sigma_lin:.6f}')

    A2 = np.vstack((x**2, x, np.ones(len(x)))).T
    s = np.linalg.lstsq(A2, y, rcond=None)[0]
    print(s)

    y_quad = s[0] * x**2 + s[1] * x + s[2]
    res_quad = y - y_quad
    SSE_quad = np.sum(res_quad**2)
    MSE_quad = SSE_quad / N
    sigma_quad = np.sqrt(SSE_quad / (N - 3)) if N > 3 else float('nan')

    print('Quadratic residuals:', res_quad)
    print(f'MSE = {MSE_quad:.6f}')
    print(f'СКО = {sigma_quad:.6f}')
