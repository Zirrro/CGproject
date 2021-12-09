import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((105, 105))  # 创建一个105x105的画布


def bresCir(x_center, y_center, r):
    if r >= 20:
        print('半径过大，可能导致圆不闭合')
    x = r
    y = 0

    xcoordinates = [x]
    ycoordinates = [y]

    # Printing the initial point the
    # axes after translation
    xcoordinates.append(x)
    ycoordinates.append(y)
    print("(", x + x_center, ", ",
          y + y_center, ")",
          sep="", end="")

    # When radius is zero only a single
    # point be printed
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

    # Initialising the value of P
    P = 1 - r

    while x > y:

        y += 1

        # Mid-point inside or on the perimeter
        if P <= 0:
            P = P + 2 * y + 1

        # Mid-point outside the perimeter
        else:
            x -= 1
            P = P + 2 * y - 2 * x + 1

        # All the perimeter points have
        # already been printed
        if (x < y):
            break

        # Printing the generated point its reflection
        # in the other octants after translation
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

        # If the generated point on the line x = y then
        # the perimeter points have already been printed
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

# def main():
#     x = int(input("x:"))
#     y = int(input("y:"))
#     r = int(input("r:"))
#     if r >= 20:
#         print('半径过大')
#         r = int(input("r:"))
#     bresCir(x, y, r)
#
#
# if __name__ == '__main__':
#     main()
