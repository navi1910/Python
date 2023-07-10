# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 08:16:42 2023

@author: Navi
"""

from tkinter import *

window = Tk()

window.title('Window1')

label1 = Label(window, text = 'First Name')
label1.grid(row = 1, column = 1)

label2 = Label(window, text = 'Last Name')
label2.grid(row = 2, column = 1)

## Entry
e1 = Entry(window)
e1.grid(row = 1, column = 2)

e2 = Entry(window)
e2.grid(row = 2, column = 2)

window.mainloop()