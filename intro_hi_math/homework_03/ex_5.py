import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from mpl_toolkits.mplot3d import Axes3D


def parallel_planes():
    fig = figure()
    ax = Axes3D(fig)
    X = np.arange(-5, 5, 0.5)
    Y = np.arange(-5, 5, 0.5)
    X, Y = np.meshgrid(X, Y)
    Z = 2 * X + 5 * Y
    Z1 = 2 * X + 5 * Y + 6
    ax.plot_wireframe(X, Y, Z)
    ax.plot_wireframe(X, Y, Z1)
    ax.scatter(0, 0, 0, 'z', 50, 'red')
    show()


def paraboloid(a=2, b=3, c=4):
    fig = figure()
    ax = Axes3D(fig)
    X = np.arange(-10, 10, 0.5)
    Y = np.arange(-10, 10, 0.5)
    X, Y = np.meshgrid(X, Y)
    Z = X ** 2 * c ** 2 / a ** 2 + Y ** 2 * c ** 2 / b ** 2
    ax.plot_wireframe(X, Y, Z)
    show()


def hyperbolic_paraboloid(a=2, b=3, c=4):
    fig = figure()
    ax = Axes3D(fig)
    X = np.arange(-100, 100, 0.5)
    Y = np.arange(-100, 100, 0.5)
    X, Y = np.meshgrid(X, Y)
    Z = X ** 2 * c ** 2 / a ** 2 - Y ** 2 * c ** 2 / b ** 2
    ax.plot_wireframe(X, Y, Z)
    show()


parallel_planes()
paraboloid()
hyperbolic_paraboloid(2, 3, 1)
