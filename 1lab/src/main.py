import matplotlib.pyplot as plt
import numpy as np
import math
import random

plt.style.use('_mpl-gallery')


def f1(x):
    return 2*math.sin(x)


def f2(x):
    return x


# make the data
arrayX = list()
arrayY = list()

arr = []
for i in range(500):
    x = random.random() * 1.895
    sigma = random.random()
    y = f1(x) + (f2(x) - f1(x)) * sigma
    arrayX.append(x)
    arrayY.append(y)


plt.scatter(arrayX, arrayY)


plt.show()
