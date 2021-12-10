import numpy as np
from scipy import interpolate

import matplotlib.pyplot as plt


def DrawBSplineCurve(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9):
    ctr = np.array([(x1, y1), (x2, y2), (x3, y3), (x4, y4),
                    (x5, y5), (x6, y6), (x7, y7), (x8, y8), (x9, y9), ])
    x = ctr[:, 0]
    y = ctr[:, 1]

    l = len(x)

    t = np.linspace(0, 1, l - 2, endpoint=True)
    t = np.append([0, 0, 0], t)
    t = np.append(t, [1, 1, 1])

    tck = [t, [x, y], 3]
    u3 = np.linspace(0, 1, (max(l * 2, 70)), endpoint=True)
    out = interpolate.splev(u3, tck)

    plt.plot(x, y, 'k--', label='Control polygon', marker='o', markerfacecolor='red')
    plt.plot(out[0], out[1], 'b', linewidth=2.0, label='B-spline curve')
    plt.legend(loc='best')
    plt.axis([min(x) - 1, max(x) + 1, min(y) - 1, max(y) + 1])
    plt.title('B-spline curve')
    plt.show()
