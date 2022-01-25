# main.py
__author__ = 'June'

# This game is about:
# Control the paddle to collect the red circle
# Collect the red circle can + 1 Score
# Beware of the black circle, if the paddle touch the black one, then you will be killed, and print" You died"
# After collect all the red one, then " print " You win"


import tkinter as tk
import time
import random
import sqlite3
import MyDBhelper
import sys

from MyRedCircle import MyRedCircle  # pull in the shape class from redcircle, blackcircle, paddle .py
from MyBlackCircle import MyBlackCircle
from MyPaddle import MyPaddle
from MyScore import MyScore  # import score class

my_conn = MyDBhelper.open_DB()
cursor = my_conn.cursor()


# define the paddle for moving left-right
def arrow_left(event):
    Paddle.move_left()


def arrow_right(event):
    Paddle.move_right()


master = tk.Tk()
windowWidth = 600
windowHeight = 500
window = tk.Canvas(master, width=600, height=500)
window.pack()

# Bind arrow keys to functions
master.bind('<Left>', arrow_left)
master.bind('<Right>', arrow_right)
master.bind('<Up>', arrow_left)
master.bind('<Down>', arrow_right)

print("Catch the Red One!!")
print("Beware of the Black One!!")

shapeList = []
for i in range(15):
    shapeList.append(
        MyRedCircle(random.randrange(0, windowWidth), random.randrange(0, windowHeight), random.randrange(1, 3),
                    random.randrange(-1, 1)))

blackList = []
for i in range(5):
    blackList.append(
        MyBlackCircle(random.randrange(0, windowWidth), random.randrange(0, windowHeight), random.randrange(2, 4),
                      random.randrange(-1, 1)))

Paddle = MyPaddle(20, 490, 0, 0)  # 50, 490, 0, 0, 10

#####Get player name######
User = input("Welcome, what is your name? My name is:")
print(User, "Start the game")


theScore = MyScore()
alive = True

while alive:

    # Move them
    for shape in shapeList:
        shape.MoveIt()
    for shape in blackList:
        shape.MoveIt()

    # Draw them
    window.delete("all")
    Paddle.DrawIt(window)  # draw the paddle
    theScore.DrawIt(window)
    for shape in shapeList:
        shape.DrawIt(window)
    for shape in blackList:
        shape.DrawIt(window)
    Paddle.DrawIt(window)
    # Paddle.logData()
    window.update()  # need to update to show screen

    # if shapeList array length equal to 0, you win
    if len(shapeList) == 0:
        print("You win")
        # change alive to false to stop the game
        alive = False

    # check paddle hits
    for idx, shape in enumerate(shapeList):
        if shape.collides(Paddle):
            # caught
            print("Catch It!", shape.showPos())  # Return string of the x,y, position of this shape#

            # add score
            theScore.Increment()

            # Once caught, remove it from the array
            del shapeList[idx]

           ######Insert player data into the table#########

            score_str = str(theScore.GetScore())

            my_conn.execute(f"INSERT INTO PLAYERSAVE (NAME, SCORE) VALUES ('{User}', NULL)")

            my_conn.execute(f"UPDATE PLAYERSAVE SET SCORE = '{score_str}'")

            my_conn.commit()

            print("Your score", score_str)


    # only check paddle hits
    for shape in blackList:
        if shape.collides(Paddle):
            print("You Died!")
            # change alive to false to stop the game
            alive = False

    # call function to check and rebound
    for shape in shapeList:
        shape.HitBorderThenBounceBack()

    for shape in blackList:
        shape.HitBorderThenBounceBack()

    # Log values (to screen)
    for shape in shapeList:
        shape.logData()

    time.sleep(0.01)  # sleep time in seconds
