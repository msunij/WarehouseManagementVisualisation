# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 20:35:50 2018

@author: msunij

"""

import string
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
warehouse = {}
sideage = 3
rows = 5
cols = 5

warehouseWidth = cols+2*sideage-1 #No use so far for this variable
warehouseHeight = rows+2*sideage-1

k = 0
for i in range(sideage, sideage+rows):
    for j in range(sideage, sideage+cols):
        warehouse[string.ascii_uppercase[k]] = [j,i]        
        k += 1
     
#initializing the entry and exit points
pointCount = 4
pointLocations = []
for i in range(sideage, sideage+cols):
    if i%2 == 1:
        pointLocations.append([i, 0])
    else:
        pointLocations.append([i, warehouseHeight])

#Creating the robot class
class Robot:
    def __init__(self, robotNumber):
        self.pos = pointLocations[robotNumber] #Assigning corresponding robot to points
        self.avail = True
        self.name = 'Robot'+str(robotNumber+1)
    
    #find the total distance robot has to travel to deliver the product
    #argument is a list of product code and delivery location
    def dist2item(self,itemCode):
        return distance(self.pos, warehouse[itemCode])
    
    def dist2exit(self,itemCode,deliveryPoint):
        return distance(warehouse[itemCode],pointLocations[deliveryPoint])

    def distanceCalculator(self,itemCode,deliveryPoint):
        return self.dist2item(itemCode) + self.dist2exit(itemCode,deliveryPoint)
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
    for key, value in inputDict.items():  
        robotIndex, itemDetail, dist = closestRobotFinder(key, value[1])
        ws.cell(row=i,column=1).value = i-1
        ws.cell(row=i,column=2).value = key
        ws.cell(row=i,column=3).value = robotList[robotIndex].name
        ws.cell(row=i,column=4).value = round(dist/robotSpeed,2)
        ws.cell(row=i,column=5).value = dist
        i += 1
    wb.save('output.xlsx')
    
def printAll(inputDict):
    for key, value in inputDict.items():
        
        closestRobotFinderPrint(key, value[1])

def closestRobotFinder(itemCode,deliveryPoint):
    closestDist = 10000 #Maximum distance that is possible
    closestIndex = 0
    for i in range(robotCount):
        if robotList[i].avail:
            dist = robotList[i].distanceCalculator(itemCode,deliveryPoint)
            if dist < closestDist:
                closestDist = dist
                closestIndex = i
    item = [itemCode,deliveryPoint]
    return [closestIndex, item, closestDist]

def closestRobotFinderPrint(itemCode,deliveryPoint):
    robotIndex, itemDetail, dist = closestRobotFinder(itemCode,deliveryPoint)
    print("Product Retrieved: {}".format(item[0]))
    print("Robot Engaged: {}".format(robotList[robotIndex].name))
    print("Distance Covered: {}meters".format(dist))
    print("Time Taken: {}seconds".format(round(dist/robotSpeed,2)))
    print("*********************************")
        
	  
def mainHardCoded():
    itemCode = 'E'
    deliveryPoint = 2
    closestRobotFinderPrint(itemCode,deliveryPoint)

def inputAsker():
    name = input('Item Code :')
    loc = int(input('Exit point :'))
    return [name, loc]

def mainLooped():
    while True:
        name, loc = inputAsker()
        closestRobotFinderPrint([name,loc])
        check = input("Check another item?(y/n): ")
        if check == 'n':
            break
        
def readExcel():
    
    from collections import OrderedDict
    
    warehouse = OrderedDict()
    #fileName = input("Enter the name of the excel file: ")
    fileName = 'warehouse.xlsx'
    workbook = openpyxl.load_workbook(fileName, data_only=True)
    sheet = workbook.active
    for i in range(2,sheet.max_row+1):
        code = sheet.cell(row=i, column=1).value
        x = sheet.cell(row=i, column=2).value
        y = sheet.cell(row=i, column=3).value
        pt = sheet.cell(row=i, column=4).value
        warehouse.update({code:[[x,y],pt]})
    return warehouse
    
        
def mainExcel():
    warehouse = readExcel()
    toExcel(warehouse)
    printAll(warehouse)
    

def main():
    res = input("""How do you want to proceed?\n
                1. From an excel file\n
                2. Manual input of Product Code[A - Y] and\n
                    delivery location[0-3]\n
                3. Quit: """)
	
    if res == '2':
        mainLooped()
    elif res == '1':
        mainExcel()
    else:
        exit()
    
if __name__ == '__main__':
    #mainHardCoded()
    #mainExcel()
    main()