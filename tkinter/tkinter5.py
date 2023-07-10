# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 08:45:29 2023

@author: Navi
"""

from tkinter import *

window = Tk()

lb = Listbox(window)

lb.insert(1, 'John')
lb.insert(2, 'Mary')
lb.insert(3, 'Peter')
lb.insert(4,'Matthew')
lb.insert(5, 'Greg')

lb.pack()

window.mainloop()
