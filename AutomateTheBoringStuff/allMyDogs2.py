# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 00:30:31 2019


dogName1 = "One"
dogName2 = "Two"
dogName3 = "Three"
dogName4 = "Four"
dogName5 = "Five"
dogName6 = "Six"

@author: Gunardi Saputra
"""
dogNames = []

while True:
    print("Enter the name of dog " + str(len(dogNames) + 1) + "(Or 'enter' to stop.): ")
    name = input()
    if name == "":
        print("Program is stop.")
        break
    dogNames = dogNames + [name] #list concatenation
print("The dog names are: ")
for name in dogNames:
    print(" " + name)