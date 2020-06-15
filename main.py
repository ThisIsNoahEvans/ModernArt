#!/bin/python3

from turtle import *
from random import *



def randomcolour():
  red = randint(0, 255)
  green = randint(0, 255)
  blue = randint(0, 255)
  color(red, green, blue)

def randomplace():
  penup()
  x = randint(-100, 100)
  y = randint(-100, 100)
  goto(x, y)
  pendown()

def randomheading():
  direction = randint(1, 360)
  setheading(direction)

def drawrectangle():
  randomcolour()
  randomplace()
  hideturtle()
  length = randint(10, 100)
  height = randint(10, 100)
  begin_fill()
  forward(length)
  right(90)
  forward(height)
  right(90)
  forward(length)
  right(90)
  forward(height)
  right(90)
  end_fill()

def drawstar(): 
  randomcolour()
  randomplace()
  randomheading()
  begin_fill()
  for side in range(5):
    left(144)
    forward(50)
  end_fill()
  
def drawtriangle():
  randomcolour()
  randomplace()
  randomheading()
  begin_fill()
  for side in range(3):
    left(50)
    forward(50)
  end_fill()




  
#shape("turtle")
#randomcolour()
#randomplace()
#randomheading()
#stamp()
#randomcolour()
#randomplace()
#randomheading()
#stamp()

clear()
setheading(0)
speed(10)

print('How many stars/rectangles do you want? (e.g. Entering 1 will draw 1 rectangle and 1 star.) ')
howmany = input()
howmany = int(howmany)

for i in range(howmany):
  drawrectangle()
  drawstar()
  drawtriangle()
