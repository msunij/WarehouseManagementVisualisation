# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 00:22:09 2018

@author: msunij
"""
import warehouse
from warehouse import itemDict,pointLocations
from tkinter import *
import time
import threading

#scaling function
def scale(num):
    if type(num) == int:
        return num*50+50
    else:
        return [scale(i) for i in num]
    
#Rectangular bounding box finder
def rectBound(pos, r):
    x1 = pos[0]-r
    y1 = pos[1]-r
    x2 = pos[0]+r
    y2 = pos[1]+r
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

#Blink green for 1 sec
def blink(loc):
    a,b,c,d = rectBound(loc,radiusItem)
    grn = canvas.create_rectangle(a,b,c,d,fill='green')
    time.sleep(.5)
    #canvas.delete(grn)
    
#draw delivery points
for pt in pointLocations:
    a,b,c,d = rectBound(scale(pt.location),radiusPt)
    canvas.create_rectangle(a,b,c,d,fill="red")

#draw product locations
for key in itemDict.keys():
    loc = itemDict[key].location
    a,b,c,d = rectBound(scale(loc),radiusItem)
    canvas.create_rectangle(a,b,c,d,fill='yellow')
    canvas.create_text(scale(loc[0]),scale(loc[1]),text=key)
    

#tkinter robot class for shapes and its motion
class RobotMotion(warehouse.Robot):
    def __init__(self, canvas,robotNumber):
        self.canvas = canvas
        super().__init__(robotNumber)
        self.pos = scale(self.pos)
        a,b,c,d = rectBound(self.pos,radiusRobot)
        self.robotIcon = self.canvas.create_oval(a,b,c,d,fill='black',tags=(self.name))
        self.robotText = self.canvas.create_text(self.pos[0],self.pos[1],text=str(robotNumber+1),fill='white',tags=self.name)
        
    def deliverThread(self,itemCode):
        print('threadstart{}{}'.format(self.name,itemCode))
        threading.Thread(target=self.deliver,args=(itemCode))
        
    def deliver(self,itemCode):
        print('inside')
        if itemDict[itemCode].stock < 1:
            print("Stock depleted")
        else:
            self.avail = False
            itemLoc = scale(itemDict[itemCode].location)
            exitPt = itemDict[itemCode].deliveryPt
            deliveryLoc = pointLocations[exitPt].location
            exitLoc = scale(deliveryLoc)
            self.move2location(itemLoc)
            blink(itemLoc)
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


robotCount = 3
robotList = []
for i in range(robotCount):
    robotList.append(RobotMotion(canvas,i))

for key in itemDict.keys():
    robotIndex, dist = warehouse.closestRobotFinder(key)
    robotList[robotIndex].deliverThread(key)
    time.sleep(.5)


root.mainloop()