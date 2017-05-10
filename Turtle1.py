angle=30
from turtle import *
speed(-1)
def draw_diamond_angle_x(x):
    color("red")
    left(x) #set cursor angle

    forward(100)
    right(60)
    forward(100)
    right(120)
    forward(100)
    right(60)
    forward(100)
    right(120)

    right(x) #return cursor angle to 0
    
for x in [angle,angle+90,angle+180,angle+270]:
    draw_diamond_angle_x(x)

left(120)
