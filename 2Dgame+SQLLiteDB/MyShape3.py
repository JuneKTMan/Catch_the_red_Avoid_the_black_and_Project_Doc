# MyShape.py
__author__ = 'June'

windowWidth = 600
windowHeight = 500


# define a base class
class MyShape3:
    # '''Make a shape for placing on Canvas'''

    def __init__(self, x=100, y=100, dx=0, dy=0, colour="#0000ff",
                 shapeNum=1):
        # '''Initialize a shape'''
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.colour = colour  # add circle colour
        self.shapeNum = shapeNum
        self.speeddx = 1
        self.speeddy = 1  # Add speed

    def logData(self):
        # '''Log shape data to a log file'''
        with open('logfile_' + str(self.shapeNum) + '.txt', 'a') as f:  # File name uses circle number
            f.write("x=" + str(self.x) + " y=" + str(self.y) + " dx=" + str(self.dx) + " dy=" + str(self.dy) + '\n')

    def MoveIt(self):
        self.x = self.x + self.dy
        self.y = self.y + self.dx

    def collides(self, other):
        if self is other:
            return False
            x_distance = abs(self.x - other.x)
            y_distance = abs(self.y - other.y)
        if (x_distance < 30) and (y_distance < 30):
            return True  # Yes, they are close
            return False

    def DrawIt(self, w):
         '''Draw the shape on the canvas, this method is overridden by subclass'''
        # w.create_rectangle(self.x - 40, self.y - 20, self.x + 50, self.y + 20, fill="#ffffff")
        # w.create_arc(self.x, self.y, self.x + 10, self.y + 10, start=0, extent=359, fill=self.colour)
        # w.create_text(self.x, self.y - 8, fill="#ff00ff", font="Times 12 italic bold",
        # text="Shape #" + str(self.shapeNum))


    def showPos(self):
        print("X: " + str(self.x) + " Y: " + str(self.y))
        return "X: " + str(self.x) + " Y: " + str(self.y)

