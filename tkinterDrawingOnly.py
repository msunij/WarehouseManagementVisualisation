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

#testing for version control


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
        self.parent = parent
        self.canvas = Canvas(root,width=600,height=600)
        self.canvas.pack()
        self.drawStructures()
        self.updatePosition()
        #self.parent.bind('<Motion>', self.motion)
        
    def testDraw(self):
        self.canvas.create_oval(50,50,100,100,fill='red')

#    def motion(self,event):
#        x, y = event.x, event.y
#        print('{}, {}'.format(x, y))
    
    def updatePosition(self):
        self.canvas.delete("robot")
        locs = [ robot.pos for robot in warehouse.robotList ]
        self.drawAllRobots(locs)
        self.parent.after(10, self.updatePosition)
        
    def drawAllRobots(self,positionList):
        for index, val in enumerate(positionList,start=1):
            self.drawRobot([index,val])
    
    def drawRobot(self,nameNpos):
        robotNumber = nameNpos[0]
        coord = nameNpos[1]
        a,b,c,d = rectBound(coord,radiusRobot)
#        if coord in [item.location for item in warehouse.itemDict.values()]:
#            self.blink(a,b,c,d)
        robotIcon = self.canvas.create_oval(a,b,c,d,fill='black',tags=("robot"))
        robotText = self.canvas.create_text(coord[0],coord[1],text=str(robotNumber),fill='white',tags="robot")
        robotPos = self.canvas.create_text(coord[0],coord[1]-20,text=self.canvas.coords(robotText),tags='robot')
   
#    def blink(self,a,b,c,d):
#        self.canvas.create_rectangle(a,b,c,d,fill='green')
    
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
    gui.after(1000,warehouse.main)
    gui.updatePosition()
    root.mainloop()