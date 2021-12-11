from PIL import Image
import sys
import os

sys.setrecursionlimit(10000)
# Window path
imgpath = os.path.join(os.getcwd(), 'imgs\\1.bmp')
# test path
# imgpath = os.path.join(os.path.abspath(os.path.dirname(os.getcwd())), 'imgs\\1.bmp')
'''
X, y:种子点，需要在填充区域内部
Filled_color:要填充的颜色
Boundary_color:边界颜色
'''
def boundary():
    im = Image.open(imgpath)
    def boundary_fill(x, y):
        filled_color = (0, 255, 255)
        boundary_color = (0, 0, 0)
        global im
        width = im.size[0]
        height = im.size[1]
        if 0 <= x < width and 0 <= y < height:
            if im.getpixel((x, y)) != filled_color and im.getpixel((x, y)) != boundary_color:
                im.putpixel((x, y), filled_color)
                boundary_fill(x + 1, y)
                boundary_fill(x - 1, y)
                boundary_fill(x, y + 1)
                boundary_fill(x, y - 1)
        return im

    Image.open(imgpath).show()
    boundary_fill(61, 25).show()
