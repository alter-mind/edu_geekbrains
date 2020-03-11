import math
from matplotlib import pyplot as plt
import numpy as np


# значения по умолчанию для y = cos(x)
def plot_cos(k=1, a=0, b=0):
    x = []
    y = []
    for i in np.arange(-12, 12, 0.1):
        x.append(i)
        y.append(k * math.cos(i - a) + b)
    plt.plot(x, y)
    plt.show()


plot_cos()
plot_cos(2, 1, 3)
plot_cos(-1, 0, 0)
