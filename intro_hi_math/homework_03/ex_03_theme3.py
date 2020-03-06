import math
from matplotlib import pyplot as plt
import numpy as np


def dec_to_pol(x, y):
    ro = math.sqrt(x ** 2 + y ** 2)
    fi = math.acos(x / ro)
    return ro, fi


def plot_circle_polar(r=5, x0=0, y0=0):
    x = []
    y1 = []
    y2 = []
    ro = []
    fi = []
    for i in np.linspace(x0 - r, x0 + r, 500):
        x.append(i)
        y1.append(math.sqrt(r ** 2 - (i - x0) ** 2) + y0)
        y2.append(-math.sqrt(r ** 2 - (i - x0) ** 2) + y0)
        pol = dec_to_pol(i, math.sqrt(r ** 2 - (i - x0) ** 2) + y0)
        ro.append(pol[0])
        fi.append(pol[1])
    plt.polar(ro, fi)
    plt.show()


def line_polar(A=1, B=1, C=1):
    ro = []
    fi = []
    for i in np.linspace(-5, 5, 500):
        pol = dec_to_pol(i, -i * A / B - C / B)
        ro.append(pol[0])
        fi.append(pol[1])
    plt.polar(ro, fi)
    plt.show()


line_polar(-2, 2, -1)