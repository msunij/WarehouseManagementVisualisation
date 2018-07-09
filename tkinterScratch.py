# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 00:21:50 2018

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
        robotCount = 1
        self.robotList = []
        for i in range(robotCount):
            self.robotList.append(RobotMotion(self.canvas,i))
        self.startWork()
        
    def startWork(self):
        for key in itemDict.keys():
            robotIndex, dist = warehouse.closestRobotFinder(key)
            self.robotList[robotIndex].deliver(key)
            time.sleep(.5)
   
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
    

#tkinter robot class for shapes and its motion
class RobotMotion(warehouse.Robot):
    def __init__(self, canvas,robotNumber):
        self.canvas = canvas
        super().__init__(robotNumber)
        self.pos = self.pos
        a,b,c,d = rectBound(self.pos,radiusRobot)
        self.robotIcon = self.canvas.create_oval(a,b,c,d,fill='black',tags=(self.name))
        self.robotText = self.canvas.create_text(self.pos[0],self.pos[1],text=str(robotNumber+1),fill='white',tags=self.name)
    
        
    def deliver(self,itemCode):
        if itemDict[itemCode].stock < 1:
            print("Stock depleted")
        else:
            self.avail = False
            itemLoc = itemDict[itemCode].location
            exitPt = itemDict[itemCode].deliveryPt
            deliveryLoc = pointLocations[exitPt].location
            exitLoc = deliveryLoc
            self.move2location(itemLoc)
            self.blink(itemLoc)
            itemDict[itemCode].removeStock()
            self.move2location(exitLoc)
            self.avail = True
        
        
    def move2location(self,location):
        dist = warehouse.displacement(self.pos,location)
        duration = dist/2
        x = (location[0]-self.pos[0])/duration
        y = (location[1]-self.pos[1])/duration
        for i in range(round(duration)):
            time.sleep(.005)
            self.canvas.move(self.name,x,y)
            self.canvas.update()
        self.pos = location
        
    #Blink green
    def blink(self,loc):
        a,b,c,d = rectBound(loc,radiusItem)
        grn = self.canvas.create_rectangle(a,b,c,d,fill='green')
        time.sleep(.5)
        #self.canvas.delete(grn)




if __name__ == "__main__":
    root = Tk()
    root.title("Intelligent Warehousing Simulation")
    gui = App(root)
    
    root.mainloop()