# -*- coding: utf-8 -*-
"""
Created on Sun May 28 22:34:21 2023

@author: Navi
"""

import Mymodule

print(Mymodule.person1)

import Mymodule as my
a = my.person1['name']
print(a)

import platform
x = platform.system()
print(x)

import platform
x = dir(platform)
print(x)