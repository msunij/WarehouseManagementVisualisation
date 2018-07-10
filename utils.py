# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 20:37:51 2018

@author: msunij
"""
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
    return hypot(pos1[0]-pos2[0],pos1[1]-pos2[1])

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
