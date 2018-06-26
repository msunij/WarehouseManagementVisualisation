# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 01:53:56 2018

@author: msunij
"""



from tkinter import *
import time

class Parent():
    def __init__(self,a,b,c,d,clr):
        self.x1 = a
        self.y1 = b
        self.x2 = c
        self.y2 = d
        self.colour = clr

class alien(Parent):
    def __init__(self, canvas,a,b,c,d,clr):
        super().__init__(a,b,c,d,clr)
        self.canvas = canvas
        self.alien1 = self.canvas.create_oval(self.x1,self.y1,self.x2,self.y2,fill=self.colour)
    def animationRight(self):
        while True:
            x = 5
            y = 0
            for i in range(0,20):
                time.sleep(0.05)
                self.canvas.move(self.alien1, x, y)
                self.canvas.update()
            break
                
    def animationLeft(self):
        while True:
            x = 5
            y = 0
            for i in range(0,51):
                time.sleep(0.025)
                self.canvas.move(self.alien1, -x, y)
                self.canvas.update()


root = Tk()
canvas = Canvas(width=400,height=400)
canvas.pack()
b = alien(canvas,200,200,250,250,'red')
b.animationRight()
root.mainloop()