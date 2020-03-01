from matplotlib import pyplot as plt
import numpy as np
import math


# по умолчанию строит окружность с центром в начале координат и радиусом 5
def plot_circle(r=5, x0=0, y0=0):
    x = []
    y1 = []
    y2 = []
    for i in np.linspace(x0 - r, x0 + r, 500):
        x.append(i)
        y1.append(math.sqrt(r ** 2 - (i - x0) ** 2) + y0)
        y2.append(-math.sqrt(r ** 2 - (i - x0) ** 2) + y0)
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.show()


# коэфициэнты даны для канонического уравнения в декатротвой системе
# x0, y0 - абсцисса и оридината центра
def plot_ellipse(a=2, b=3, x0=0, y0=0):
    x = []
    y1 = []
    y2 = []
    for i in np.linspace(x0 - a, x0 + a, 500):
        x.append(i)
        y1.append(y0 + math.sqrt((1 - ((i - x0) ** 2) / a ** 2) * b ** 2))
        y2.append(y0 - math.sqrt((1 - ((i - x0) ** 2) / a ** 2) * b ** 2))
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.show()


# коэфициэнты даны для канонического уравнения в декатротвой системе
# x0, y0 - абсцисса и оридината центра
def plot_hyperbola(a=2, b=3, y0=0, x0=0):
    x = []
    y1 = []
    y2 = []
    for i in np.linspace(x0 - a, x0 + a, 500):
        x.append(i)
        y1.append(y0 + math.sqrt((1 + ((i - x0) ** 2) / a ** 2) * b ** 2))
        y2.append(y0 - math.sqrt((1 + ((i - x0) ** 2) / a ** 2) * b ** 2))
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.show()


print('Окружность:')
plot_circle()
input()

print('Эллипс:')
plot_ellipse()
input()

print('Гипербола')
plot_hyperbola()
