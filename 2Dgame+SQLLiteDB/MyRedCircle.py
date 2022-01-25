__author__ = 'June'

from MyShape3 import MyShape3
import random


class MyRedCircle(MyShape3):
    pass

    def DrawIt(self, w):
        # '''Draw the shape on the canvas, this method is overridden by subclass'''
        w.create_arc(self.x, self.y, self.x + 10, self.y + 10, start=0, extent=359, fill="#ff0000")

    def collides(self, other):
        if self is other:
            return False
        x_distance = abs(self.x - other.x)
        y_distance = abs(self.y - other.y)
        if (x_distance < 20) and (y_distance < 20):
           return True  # Yes, they are close
        return False

    def HitBorderThenBounceBack(self):
        if self.x <= 5 or self.x >= 600 - 5:
            self.dy = - self.dy
        if self.y <= 5 or self.y >= 500 - 5:
            self.dx = - self.dx
