import matplotlib.pyplot as plt


def DrawBezeriCurve(x1, y1, x2, y2, x3, y3):
    x = [x1, x2, x3]
    y = [y1, y2, y3]
    xLast = []
    yLast = []
    cnt = 10

    def getValue(x1, x2, t):
        return x1 + (x2 - x1) * t

    def PointTest():
        for i in range(len(x)):
            plt.text(x[i], y[i], 'P' + str(i))
        return

    def BezierPoint():
        for i in range(len(xLast)):
            plt.plot(xLast[i], yLast[i], '*')
        return

    def Draw(x, y, num):
        if num == 3:
            x0 = getValue(x[0], x[1], i / cnt)
            y0 = getValue(y[0], y[1], i / cnt)
            x1 = getValue(x[1], x[2], i / cnt)
            y1 = getValue(y[1], y[2], i / cnt)
            plt.plot([x0, x1], [y0, y1])
            xLast.append(getValue(x0, x1, i / cnt))
            yLast.append(getValue(y0, y1, i / cnt))
            plt.plot(xLast[i], yLast[i], '*')
            plt.pause(0.2)
        else:
            xNext = []
            yNext = []
            for j in range(num - 1):
                xNext.append(getValue(x[j], x[j + 1], i / cnt))
                yNext.append(getValue(y[j], y[j + 1], i / cnt))
            plt.plot(xNext, yNext)
            plt.pause(0.2)
            Draw(xNext, yNext, num - 1)
        return

    def Show():
        plt.grid(True)
        plt.plot(x, y)
        PointTest()
        BezierPoint()
        return

    for i in range(cnt + 1):
        Draw(x, y, len(x))
        plt.pause(1)
        plt.cla()
        Show()

    plt.cla()
    Show()
    plt.plot(xLast, yLast)
    plt.show()


# def main():
#     DrawBezeriCurve(1,1,6,13,15,0)
#
#
# if __name__ == '__main__':
#     main()

# https://blog.csdn.net/qq_47867028/article/details/116355539
