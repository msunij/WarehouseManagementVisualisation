# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 20:35:50 2018

@author: msunij

"""

import openpyxl
from math import hypot



#Utility Functions

#this function needs to be edited
def distanceMatrix():
    for letter in string.ascii_uppercase[:9]:
        print(letter,end=" :")
        for i in range(3):
            print(robotList[i].distanceDict[letter],end=",")
        print(" ")

#find the current positions of the robots 
def robotsPositions():
    for rob in robotList:
        print(rob.name, rob.pos)
        
#to calculate the distance between two points
def distance(pos1, pos2):
    dist = abs(pos1[0]-pos2[0])+abs(pos1[1]-pos2[1])
    return dist

def displacement(pos1, pos2):
    return hypot(pos1[0]-pos2[1],pos1[1]-pos2[1])
        
robotSpeed = 1.5

#initializing the warehouse data point
sideage = 3
rows = 5
cols = 5

warehouseWidth = cols+2*sideage-1 #No use so far for this variable
warehouseHeight = rows+2*sideage-1

class Item:
    def __init__(self,itemName,location,stockLevel=5,deliveryPt=0):
        self.name = itemName
        self.location = location
        self.stock = stockLevel
        self.deliveryPt = deliveryPt
        
    def addStock(self,quantity):
        self.stock += quantity
    
    def removeStock(self,quantity=1):
        self.stock -= quantity


def readExcel():
        
    D = dict()
    #fileName = input("Enter the name of the excel file: ")
    fileName = 'warehouseData.xlsx'
    workbook = openpyxl.load_workbook(fileName, data_only=True)
    sheet = workbook.active
    for i in range(2,sheet.max_row+1):
        code = sheet.cell(row=i, column=2).value
        x = sheet.cell(row=i, column=3).value
        y = sheet.cell(row=i, column=4).value
        name = sheet.cell(row=i, column=5).value
        stock = sheet.cell(row=i, column=6).value
        deliveryPt = sheet.cell(row=i, column=7).value
        
        D[code] = Item(name,[x,y],stock,deliveryPt)
    return D
    
  
#initializing the entry and exit points
class ExitPoint:
    def __init__(self,location):
        self.location = location
        
        
pointCount = 4
pointLocations = []
for i in range(sideage, sideage+cols):
    if i%2 == 1:
        pointLocations.append(ExitPoint([i, 0]))
    else:
        pointLocations.append(ExitPoint([i, warehouseHeight]))



#Creating the robot class
class Robot:
    def __init__(self, robotNumber):
        self.pos = pointLocations[robotNumber].location #Assigning corresponding robot to points
        self.avail = True
        self.name = 'Robot'+str(robotNumber+1)
    
    #find the total distance robot has to travel to deliver the product
    #argument is a list of product code and delivery location
    def dist2item(self,itemCode):
        return distance(self.pos, itemDict[itemCode].location)
    
    def dist2exit(self,itemCode):
        pt = itemDict[itemCode].deliveryPt
        return distance(itemDict[itemCode].location,pointLocations[pt].location)

    def distanceCalculator(self,itemCode):
        return self.dist2item(itemCode) + self.dist2exit(itemCode)
robotCount = 3

robotList = [ Robot(i) for i in range(robotCount)]

def toExcel(inputDict):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws['A1'] = 'Sl No.'
    ws['B1'] = 'ProductCode'
    ws['C1'] = 'RobotEngaged'
    ws['D1'] = 'TimeTaken'
    ws['E1'] = 'DistanceCovered'
    i = 2
    for key in inputDict.keys():  
        robotIndex, dist = closestRobotFinder(key)
        ws.cell(row=i,column=1).value = i-1
        ws.cell(row=i,column=2).value = itemDict[key].name
        ws.cell(row=i,column=3).value = robotList[robotIndex].name
        ws.cell(row=i,column=4).value = round(dist/robotSpeed,2)
        ws.cell(row=i,column=5).value = dist
        i += 1
    wb.save('output.xlsx')
    
def printAll(inputDict):
    for key in inputDict.keys():
        
        closestRobotFinderPrint(key)

def closestRobotFinder(itemCode):
    closestDist = 10000 #Maximum distance that is possible
    closestIndex = 0
    for i in range(robotCount):
        if robotList[i].avail:
            dist = robotList[i].distanceCalculator(itemCode)
            if dist < closestDist:
                closestDist = dist
                closestIndex = i
    return [closestIndex, closestDist]

def closestRobotFinderPrint(itemCode):
    robotIndex, dist = closestRobotFinder(itemCode)
    print("Product Retrieved: {}".format(itemDict[itemCode].name))
    print("Robot Engaged: {}".format(robotList[robotIndex].name))
    print("Distance Covered: {}meters".format(dist))
    print("Time Taken: {}seconds".format(round(dist/robotSpeed,2)))
    print("*********************************")


itemDict = readExcel()

if __name__ == '__main__':
    toExcel(itemDict)
    printAll(itemDict)