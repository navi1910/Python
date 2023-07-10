# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 08:49:45 2023

@author: Navi
"""

from tkinter import *

window = Tk()

main_menu = Menu(window)

# Menu
window.config(menu = main_menu)

# File
file_menu = Menu(main_menu)

main_menu.add_cascade(label = 'File', menu = file_menu)
file_menu.add_command(label = 'New')
file_menu.add_command(label = 'Open')

file_menu.add_separator()

file_menu.add_command(label = 'Exit')

# Help
help_menu = Menu(main_menu)

main_menu.add_cascade(label = 'Help', menu = help_menu)
help_menu.add_command(label = 'About')

# Entry
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



