# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 00:22:09 2018

@author: msunij
"""
import warehouse
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



#draw delivery points
for pt in warehouse.pointLocations:
    a,b,c,d = rectBound(scale(pt),radiusPt)
    canvas.create_rectangle(a,b,c,d,fill="red")
    
#draw product locations
for key,value in warehouse.warehouse.items():
    a,b,c,d = rectBound(scale(value),radiusItem)
    canvas.create_rectangle(a,b,c,d,fill='yellow')
    
##draw robot
#for rob in warehouse.robotList:
#    a,b,c,d = rectBound(rob.pos,radiusRobot)
#    canvas.create_rectangle(a,b,c,d,fill='black')
    
#tkinter class for shapes and its motion
class RobotMotion(warehouse.Robot):
    def __init__(self, canvas,robotNumber):
        self.canvas = canvas
        super().__init__(robotNumber)
        self.pos = scale(self.pos)
        a,b,c,d = rectBound(self.pos,radiusRobot)
        self.robotIcon = self.canvas.create_oval(a,b,c,d,fill='black')
        
    def move2exit(self,itemDetail):
        itemPt = scale(database[itemDetail[0]][0])
        exitPt = scale(warehouse.pointLocations[itemDetail[1]])
        self.move2location(itemPt)
        self.move2location(exitPt)
        
        
    def move2location(self,location):
        dist = warehouse.displacement(self.pos,location)
        duration = dist/2
        x = (location[0]-self.pos[0])/duration
        y = (location[1]-self.pos[1])/duration
        for i in range(round(duration)):
            time.sleep(.005)
            self.canvas.move(self.robotIcon,x,y)
            self.canvas.update()
        self.pos = location
        
#class RobotThread(threading.Thread):
#    def __init__(self,rob,itemDetail):
#        self.rob = rob
#    
#    def run(self):
#        self.rob.move2exit(itemDetail)

robotCount = 3
#robotList = [ RobotMotion(canvas,i) for i in range(robotCount)]
robotList = []
for i in range(robotCount):
    robotList.append(RobotMotion(canvas,i))
    t = threading.Thread(target=robotList[i].move2exit,\
                         name=robotList[i].name+'thread',\
                         args=())

database = warehouse.readExcel()
for key, value in database.items():
    robotIndex, itemDetail, dist = warehouse.closestRobotFinder(key,value[1])
    robotList[robotIndex].move2exit(itemDetail)


root.mainloop()