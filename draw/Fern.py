import matplotlib.pyplot as plt
from random import randint

def DrawFern():
    x = []
    y = []

    x.append(0)
    y.append(0)

    current = 0

    for i in range(1, 50000):

        z = randint(1, 100)

        if z == 1:
            x.append(0)
            y.append(0.16 * (y[current]))

        # 0.85
        if z >= 2 and z <= 86:
            x.append(0.85 * (x[current]) + 0.04 * (y[current]))
            y.append(-0.04 * (x[current]) + 0.85 * (y[current]) + 1.6)

        # 0.07
        if z >= 87 and z <= 93:
            x.append(0.2 * (x[current]) - 0.26 * (y[current]))
            y.append(0.23 * (x[current]) + 0.22 * (y[current]) + 1.6)

        # 0.07
        if z >= 94 and z <= 100:
            x.append(-0.15 * (x[current]) + 0.28 * (y[current]))
            y.append(0.26 * (x[current]) + 0.24 * (y[current]) + 0.44)

        current = current + 1

    plt.scatter(x, y, s=0.2, edgecolor='green')

    plt.show()
