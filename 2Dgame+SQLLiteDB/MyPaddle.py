__author__ = 'June'

from MyShape3 import MyShape3
import time
import tkinter



class MyPaddle(MyShape3):
    pass

    def __init__(self, x=100, y=100, dx=0, dy=0, colour="#0000ff", shapeNum=1):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.colour = colour
        self.shapeNum = shapeNum

    def DrawIt(self, w):
        super()
        w.create_rectangle(self.x - 20, self.y - 10, self.x + 40, self.y + 10, fill=self.colour)


    def move_left(self):
        if (self.x - 20) >= 40:
            self.x = self.x - 20
        else:
            self.x = 40

    def move_right(self):
        if (self.x + 20) <= 560:
            self.x = self.x + 20
        else:
            self.x = 560
