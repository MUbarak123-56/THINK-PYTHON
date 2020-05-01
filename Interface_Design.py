#!/bin/python3
import math
import turtle
bob = turtle.Turtle()
def polygon(t, length, n):
  for i in range(n):
    t.fd(length)
    t.lt(360/n)

def arc(t,r,angle):
  circumference = 2 * (angle/57.3) * r
  n = int(circumference/3) + 3
  length = circumference / n 
  step_angle = angle / n
  for i in range(n): 
    t.fd(length) 
    t.lt(step_angle) 
def circle(t, r):
  arc(t, r, 360) 
sam = turtle.Turtle()
arc(sam,50,150)
turtle.mainloop()
