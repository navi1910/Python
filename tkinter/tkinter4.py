# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 08:29:05 2023

@author: Navi
"""

from tkinter import *

window = Tk()

e = Entry(window, width = 50, font = ('Calibri', 30))
e.pack()
e.insert(0,'Enter Name: ')

def my_button():
    string = 'Hello my name is ' + e.get().split(':')[1]
    
    my_label = Label(window, text = string, font = ('Ariel', 35))
    
    e.delete(0, 'end')
    
    my_label.pack()


button = Button(window, text = 'Click to Display', command = my_button,
                width = 40, bg = 'Black', fg = 'White', font = 35)
button.pack()

window.mainloop()