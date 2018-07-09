# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 21:33:36 2018

@author: msunij
"""

import warehouse
from warehouse import itemDict,pointLocations
from utils import *
from tkinter import *
import threading
import time


radiusPt = 20
radiusItem = 15
radiusRobot = 10

X1 = scale(0)
Y1 = scale(0)
X2 = scale(10)
Y2 = scale(10)

class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.canvas = Canvas(root,width=600,height=600)
        self.canvas.pack()
        self.drawStructures()
        self.drawRect()
        
    def drawRobot(self):
        self.canvas.create_rectangle(300,300,600,600,fill="blue")
   
    def drawStructures(self):
        floor = self.canvas.create_rectangle(X1,Y1,X2,Y2,fill="lightblue")
        #draw delivery points
        for pt in pointLocations:
            a,b,c,d = rectBound(pt.location,radiusPt)
            self.canvas.create_rectangle(a,b,c,d,fill="red")
        #draw product locations
        for key in itemDict.keys():
            loc = itemDict[key].location
            a,b,c,d = rectBound(loc,radiusItem)
            self.canvas.create_rectangle(a,b,c,d,fill='yellow')
            self.canvas.create_text(loc[0],loc[1],text=key)
    


if __name__ == "__main__":
    root = Tk()
    root.title("Intelligent Warehousing Simulation")
    gui = App(root)

    root.mainloop()