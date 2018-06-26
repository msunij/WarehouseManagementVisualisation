# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 01:53:56 2018

@author: msunij
"""

from tkinter import *
import time

root = Tk()
canvas = Canvas(root, width=300,height=400)
canvas.pack()

red_line = canvas.create_line(0,0,150,200,fill='red')
red = canvas.create_oval(20,20,40,40,fill='red')
for x in range(0,120):
    canvas.move(1,5,0)
    root.update()
    time.sleep(0.10)


root.mainloop()