# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 23:49:56 2019

@author: Gunardi Saputra
"""

def spam():
    eggs = "spam local"
    print(eggs) # prints "spam local"
    
def bacon():
    eggs = "bacon local"
    print(eggs) # prints "bacon local"
    spam()
    print(eggs) #prints "bacon local"

eggs = "global"
bacon()
print(eggs) #prints "global"
