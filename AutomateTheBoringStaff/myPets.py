# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 01:06:29 2019

@author: Gunardi Saputra

Adding myPets.py

"""
myPets = ["One", "Two", "Three"]
print("Enter a pet name: ")
name = input()
if name not in myPets:
    print("I do not have a pet named " + name)
else:
    print(name + " is my pet.")
