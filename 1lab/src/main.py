import matplotlib.pyplot as plt
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

x_max = 1.895
for i in range(2000):
    x = random.random() * x_max
    sigma = random.random()
    y = f2(x) + (f1(x) - f2(x)) * sigma
    arrayX.append(x)
    arrayY.append(y)


plt.scatter(arrayX, arrayY)
plt.show()
