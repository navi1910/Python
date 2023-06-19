# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 08:44:00 2023

@author: Navi
"""

class math:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def multiply(self,x,y):
        return x*y
    
    def add(self,x,y):
        return x+y
    
    def x_even(self, x):
        if x%2 == 0:
            print('x is even.')
        else:
            print('x is not even.')
            
            
import os
os.getcwd()
os.chdir('E://Besant Python')          
