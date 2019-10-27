# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 13:45:08 2019

@author: Gunardi Saputra
"""

birthdays = {"A": "Jan 1", "B": "Feb 2", "C": "Mar 3"}

while True:
    print("Enter a name: (blank to quit)")
    name = input()
    if name == "":
        print("Program is stop.")
        break
            
    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)
    else:
        print("I do not have birthday information for " + name)
        print("What is the birthday?")
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated.")
