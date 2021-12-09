from turtle import *


# Alphabet : F
# Constants : +, ?
# Axiom : F
# Production rules: F ? F+F–F+F

# function to create koch curve
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


# main function
if __name__ == "__main__":
    # defining the speed of the turtle
    speed(0)
    length = 300.0

    # Pull the pen up – no drawing when moving.
    penup()

    # Move the turtle backward by distance,
    # opposite to the direction the turtle
    # is headed.
    # Do not change the turtle’s heading.
    backward(length / 2.0)

    # Pull the pen down – drawing when moving.
    pendown()

    snowflake(length, 5)

    # To control the closing windows of the turtle
    mainloop()

# https://www.geeksforgeeks.org/koch-curve-koch-snowflake/
