# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 13:40:01 2019

@author: Gunardi Saputra

Adding passingReference.py
"""

def eggs(somePar):
    somePar.append("Hello")
    
spam = [1, 2, 3]
eggs(spam)
print(spam)