# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 20:35:50 2018

@author: msunij

"""

import string

def distanceMatrix():
    for letter in string.ascii_uppercase[:9]:
        print(letter,end=" :")
        for i in range(3):
            print(robotList[i].distanceDict[letter],end=",")
        print(" ")
        
def robotsPositions():
    for rob in robotList:
        print(rob.name, rob.pos)

robotSpeed = 1.5
#initializing the Warehouse data point
wareHouseWidth = 5
wareHouseHeight = 7

wareHouse = {}
frontage = 3
sideage = 1
rows = 3
cols = 4

k = 0
for i in range(frontage, frontage+rows):
    for j in range(sideage, sideage+cols):
        wareHouse[string.ascii_uppercase[k]] = [j,i]        
        k += 1
     
#initializing the entry and exit points
pointCount = 4
pointLocations = []
for i in range(pointCount):
    if i%2 == 0:
        pointLocations.append([i+1, 0])
    else:
        pointLocations.append([i+1, wareHouseHeight])

class robot:
    def __init__(self, robotNumber):
        self.pos = pointLocations[robotNumber]#Assigning corresponding robot to points
        self.avail = True
        self.name = 'Robot'+str(robotNumber+1)
        
    def distanceCalculator(self,item):
        dist2item = abs(self.pos[0]-wareHouse[item[0]][0])+abs(self.pos[1]-wareHouse[item[0]][1])
        dist2exit = abs(pointLocations[item[1]][0]-wareHouse[item[0]][0])+abs(pointLocations[item[1]][1]-wareHouse[item[0]][1])
        distance = dist2item+dist2exit
        return distance

robotCount = 3

robotList = [ robot(i) for i in range(robotCount)]

def closestRobotFinder(item):
    closestDist = 10000 #Maximum distance that is possible
    closestIndex = 0
    for i in range(robotCount):
        if robotList[i].avail:
            dist = robotList[i].distanceCalculator(item)
            if dist < closestDist:
                closestDist = dist
                closestIndex = i
        
    robot2use = robotList[closestIndex]
    robot2use.pos = pointLocations[item[1]]
    return [robot2use.name, closestDist]

def printOutput(item):
	robotNumber, timeTaken = closestRobotFinder(item)
	print("Robot Engaged: {}".format(robotNumber))
	print("Distance Covered: {}meters".format(timeTaken))
	print("Time Taken: {}seconds".format(timeTaken*robotSpeed))
	  
def mainHardCoded():
	item2retrive = ['E', 3]
	printOutput(item2retrive)

def inputAsker():
    name = input('Item Code :')
    loc = int(input('Exit point :'))
    return [name, loc]

def mainLooped():
    while True:
        name, loc = inputAsker()
        printOutput([name,loc])
        check = input("Check another item?(y/n): ")
        if check == 'n':
            break
        
def mainFromFile():
    fileName = input("Enter the name of the excel file: ")
    data = read_excel(fileName)
    
        
mainHardCoded()