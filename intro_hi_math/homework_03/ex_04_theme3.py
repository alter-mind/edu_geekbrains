from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import fsolve


def f(x):
    return x ** 2 - 1


def g(x):
    return (np.exp(x) - 1) / x - 1


def plot_f_g():
    x = np.linspace(-3, 5.5, 201)
    plt.plot(x, f(x))
    plt.plot(x, g(x))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


def equations(p):
    x, y = p
    return y - x ** 2 + 1, np.exp(x) + x * (1 - y) - 1


def numerical_method():
    x1, y1 = fsolve(equations, (-1, 1))
    x2, y2 = fsolve(equations, (0, 5))
    x3, y3 = fsolve(equations, (2, 3))
    x4, y4 = fsolve(equations, (4, 5))
    print(f'численное решение системы уравнений:\n'
          f'x1 = {x1} y22030836699761 = {y1};\n'
          f'x2 = {x2} y2 = {y2};\n'
          f'x3 = {x3} y3 = {y3};\n'
          f'x4 = {x4} y4 = {y4}')


def inequality_graph():
    x = np.linspace(-3, 5, 201)
    plt.plot(x, np.exp(x) + x * (2 - x ** 2) - 1)
    plt.plot([-3, 5], [0, 0], color='red', linewidth=1.75, linestyle='--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()


print('Решение системы уравнений графически: ')
input()
plot_f_g()
print('Решение системы уравнений численным методом с помощью библиотеки scipy: ')
input()
numerical_method()
print('Решение системы неравенств путем сведения к одной функции (графически): ')
input()
inequality_graph()
