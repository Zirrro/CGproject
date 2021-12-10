import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((105, 105))


def bresCir(x_center, y_center, r):
    if r >= 20:
        print('半径过大，可能导致圆不闭合')
    x = r
    y = 0

    xcoordinates = [x]
    ycoordinates = [y]

    xcoordinates.append(x)
    ycoordinates.append(y)
    print("(", x + x_center, ", ",
          y + y_center, ")",
          sep="", end="")

    if (r > 0):
        print("(", x + x_center, ", ",
              -y + y_center, ")",
              sep="", end="")
        xcoordinates.append(x + x_center)
        ycoordinates.append(-y + y_center)

        print("(", y + x_center, ", ",
              x + y_center, ")",
              sep="", end="")
        xcoordinates.append(y + x_center)
        ycoordinates.append(x + y_center)

        print("(", -y + x_center, ", ",
              x + y_center, ")", sep="")
        xcoordinates.append(-y + x_center)
        ycoordinates.append(x + y_center)

    P = 1 - r

    while x > y:

        y += 1

        if P <= 0:
            P = P + 2 * y + 1

        else:
            x -= 1
            P = P + 2 * y - 2 * x + 1

        if (x < y):
            break

        print("(", x + x_center, ", ", y + y_center,
              ")", sep="", end="")
        xcoordinates.append(x + x_center)
        ycoordinates.append(y + y_center)

        print("(", -x + x_center, ", ", y + y_center,
              ")", sep="", end="")
        xcoordinates.append(-x + x_center)
        ycoordinates.append(y + y_center)

        print("(", x + x_center, ", ", -y + y_center,
              ")", sep="", end="")
        xcoordinates.append(x + x_center)
        ycoordinates.append(-y + y_center)

        print("(", -x + x_center, ", ", -y + y_center,
              ")", sep="")
        xcoordinates.append(-x + x_center)
        ycoordinates.append(-y + y_center)

        if x != y:
            print("(", y + x_center, ", ", x + y_center,
                  ")", sep="", end="")
            xcoordinates.append(y + x_center)
            ycoordinates.append(x + y_center)

            print("(", -y + x_center, ", ", x + y_center,
                  ")", sep="", end="")
            xcoordinates.append(-y + x_center)
            ycoordinates.append(x + y_center)

            print("(", y + x_center, ", ", -x + y_center,
                  ")", sep="", end="")
            xcoordinates.append(y + x_center)
            ycoordinates.append(-x + y_center)

            print("(", -y + x_center, ", ", -x + y_center,
                  ")", sep="")
            xcoordinates.append(-y + x_center)
            ycoordinates.append(-x + y_center)

        plt.plot(xcoordinates, ycoordinates, 'o')
        plt.show()
