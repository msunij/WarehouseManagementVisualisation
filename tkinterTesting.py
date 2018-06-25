# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 01:53:56 2018

@author: msunij
"""

from tkinter import *

pL = [[3, 0], [4, 10], [5, 0], [6, 10], [7, 0]]

#Circle bounding box finder
def circleBound(a,b, r):
    x1 = a-r
    y1 = b-r
    x2 = a+r
    y2 = b+r
    return [x1,y1,x2,y2]


root = Tk()

canvas = Canvas(root,width=600,height=600)
canvas.pack()
for pt in pL:
    radius = 10
    a,b,c,d = circleBound(pt[0]*50,pt[1]*50,radius)
    circle = canvas.create_oval(a,b,c,d,fill = 'red')

root.mainloop()