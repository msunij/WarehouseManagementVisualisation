# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 00:22:09 2018

@author: msunij
"""
import warehouse
from tkinter import *

#scaling function
def scale(num):
    return num*50+50

#Circle bounding box finder
def rectBound(a,b, r):
    x1 = a-r
    y1 = b-r
    x2 = a+r
    y2 = b+r
    return [x1,y1,x2,y2]

    
    
root = Tk()

canvas = Canvas(root,width=600,height=600)
canvas.pack()

radiusPt = 20
radiusItem = 15
radiusRobot = 10

X1 = scale(0)
Y1 = scale(0)
X2 = scale(10)
Y2 = scale(10)

floor = canvas.create_rectangle(X1,Y1,X2,Y2,fill="lightblue")



#draw delivery points
for pt in warehouse.pointLocations:
    a,b,c,d = rectBound(scale(pt[0]),scale(pt[1]),radiusPt)
    canvas.create_oval(a,b,c,d,fill="red")
    
#draw product locations
for key,value in warehouse.warehouse.items():
    a,b,c,d = rectBound(scale(value[0]),scale(value[1]),radiusItem)
    canvas.create_rectangle(a,b,c,d,fill='yellow')
    
#draw robot
for rob in warehouse.robotList:
    x,y = rob.pos
    a,b,c,d = rectBound(scale(x),scale(y),radiusRobot)
    canvas.create_rectangle(a,b,c,d,fill='black')
    
#tkinter class for shapes and its motion
class Shape:
    def __init__(self, master):
        

    

    
root.mainloop()