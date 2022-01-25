__author__ = 'June'

from MyShape3 import MyShape3
import random

class MyBlackCircle(MyShape3):
    pass

    def DrawIt(self, w):
        w.create_arc(self.x, self.y, self.x + 20, self.y + 20, start=0, extent=359, fill="#000000")

    # Black dot re-bouce when reach x, y , dx, dy don't re-bounce
    def MoveIt(self):
        self.x = self.y + self.dy
        self.y = self.x + self.dx

        if self.x <= 0:
            self.dy = self.speeddy * 3

        if self.y <= 0:
            self.dx = self.speeddx * 3

        if self.x >= 600:
            self.dy = self.speeddy * 3

        if self.y >= 500:
            self.dy = self.speeddy * 3

    def collides(self, other):
        if self is other:
            return False
        x_distance = abs(self.x - other.x)
        y_distance = abs(self.y - other.y)
        if (x_distance < 30) and (y_distance < 30):
            return True  # Yes, they are close
        return False

    def HitBorderThenBounceBack(self):
        if self.x <= 10 or self.x >= 600 - 10:
            self.dy = - self.dy
        if self.y <= 10 or self.y >= 500 - 10:
            self.dx = - self.dx
