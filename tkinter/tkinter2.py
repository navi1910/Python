# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 08:14:08 2023

@author: Navi
"""

import tkinter as tk
from tkinter import *

window = tk.Tk()

window.title('My window')
'''
def my_button():
    print('The button was clicked.')

button = tk.Button(window, text = 'Stop',
                   command = window.destroy,
                   bg = 'Yellow',
                   activebackground='Blue',
                   width = 10,
                   height = 10)

button.pack()

w = Canvas(window, width = 400, height = 600, bg = 'Orange')

w.pack()

w.create_line(0, 300, 100, 300)'''

'''var1 = IntVar()

Checkbutton(window, text = 'Yes', variable = var1).grid(row = 0,
                                                        sticky = W)

var2 = IntVar()
Checkbutton(window, text = 'No', variable = var2).grid(row = 1,
                                                        sticky = W)
'''
frame = Frame(window)
frame.pack()

redbutton = Button(frame, text = 'Red', bg = 'Red')
redbutton.pack(side = BOTTOM)

greenbutton = Button(frame, text = 'Green', bg = 'Green')
greenbutton.pack(side = LEFT)

bluebutton = Button(frame, text = 'Blue', bg = 'Blue')
bluebutton.pack()

bframe = Frame(window)
bframe.pack(side = BOTTOM)

blackbutton = Button(bframe, text = 'Black', fg = 'White', bg = 'Black')
blackbutton.pack(side = BOTTOM)

window.mainloop()








