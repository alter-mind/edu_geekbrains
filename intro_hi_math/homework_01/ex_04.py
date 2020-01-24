import matplotlib.pyplot as plt
import numpy as np
import random

k = random.random()
x = np.linspace(-10, 10, 256)
plt.plot(x, np.cos(x))
plt.plot(x, np.cos(k*x))
plt.show()