# My Score
__author__ = 'June'

from MyShape3 import MyShape3



class MyScore(MyShape3):  # add score to canvas
    pass

    def __init__(self, x=400, y=30, colour="#ffffff"):
        self.x = x
        self.y = y
        self.colour = colour
        self.score = 0

    def Increment(self):
        self.score = self.score + 1
        print("Your score -->", self.score)

    def SetScore(self, newScore):
        self.score = newScore

    def GetScore(self):
        return self.score

    def DrawIt(self, w):
        super()

        w.create_rectangle(self.x - 40, self.y - 20, self.x + 50, self.y + 12, fill=self.colour)
        w.create_text(self.x, self.y - 8, fill="#ff00ff", font="Times 12 italic bold", text="Score=" + str(self.score))
