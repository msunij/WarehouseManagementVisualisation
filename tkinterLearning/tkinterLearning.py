# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 20:32:44 2018

@author: msunij
"""

# Tkinter animate via canvas.move(obj, xAmount, yAmount)
import tkinter as tk
import time
root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
# canvas.create_rectangle(x0, y0, x1, y1, option, ... )
# x0, y0, x1, y1 are corner coordinates of ulc to lrc diagonal
blue_rect = canvas.create_rectangle(20, 260, 120, 360, outline='white', fill='blue')
red_rect = canvas.create_rectangle(20, 10, 120, 110, outline='white', fill='red')
for x in range(50):
    y = x = 5
    time.sleep(1)
    canvas.move(blue_rect, x, -y)
    canvas.move(red_rect, x, y)
    canvas.update()
root.mainloop()