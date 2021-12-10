from turtle import *


def snowflake(lengthSide, levels):
    if levels == 0:
        forward(lengthSide)
        return
    lengthSide /= 3.0
    snowflake(lengthSide, levels - 1)
    left(60)
    snowflake(lengthSide, levels - 1)
    right(120)
    snowflake(lengthSide, levels - 1)
    left(60)
    snowflake(lengthSide, levels - 1)


def DrawKoch():
    speed(0)
    length = 300.0
    penup()
    backward(length / 2.0)
    pendown()
    snowflake(length, 4)
    mainloop()


if __name__ == "__main__":
    speed(0)
    length = 300.0
    penup()
    backward(length / 2.0)
    pendown()
    snowflake(length, 5)
    mainloop()
