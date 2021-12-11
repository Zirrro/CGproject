from PIL import Image
import sys
import tkinter as tk
from tkinter import filedialog

def boundary(x, y):
    sys.setrecursionlimit(10000)
    # 获取图片路径
    root = tk.Tk()
    root.withdraw()
    imgpath = filedialog.askopenfilename()
    global im
    im = Image.open(imgpath)
    # 对图片进行区域填充
    def boundary_fill(x, y):
        filled_color = (0, 255, 255)
        boundary_color = (0, 0, 0)
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
    boundary_fill(x, y).show()
