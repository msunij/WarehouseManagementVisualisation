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

wareHouse = {}
exitPos = [0,9]

k = 0
for i in range(7,10):
    for j in range(1,4):
        wareHouse[string.ascii_uppercase[k]] = [j,i]        
        k += 1
        
class robot:
    def __init__(self,pos):
        self.pos = pos+1
        self.avail = True
        self.distanceDict = {item:self.distanceCalculator(item) for item in wareHouse.keys()}
    
    def distanceCalculator(self,itemName):
        dist2item = abs(self.pos-wareHouse[itemName][0])+wareHouse[itemName][1]
        dist2exit = wareHouse[itemName][0]+abs(exitPos[1]-wareHouse[itemName][1])
        distance = dist2item+dist2exit
        return distance

item2retrive = 'D'
robotCount = 3
robotList = [ robot(i) for i in range(robotCount)]

def closestRobotFinder(item2retrive):
    closest = 10000 #Maximum distance that is possible
    closestIndex = 0
    for i in range(robotCount):
        if robotList[i].avail:
            if robotList[i].distanceDict[item2retrive] < closest:
                closest = robotList[i].distanceDict[item2retrive]
                closestIndex = i
    return closestIndex

robot2use = robotList[closestRobotFinder(item2retrive)]

