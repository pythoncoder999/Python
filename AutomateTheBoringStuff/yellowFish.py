# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 22:45:27 2019

@author: Gunardi Saputra
"""

while True:
    print("What's your name?")
    name = input()
    if name != "Nathan":
        continue
    print("Hello, " + name + ". What is the password?")
    password = input()
    if password == "yellowFish":
        break
print(name + ", Access granted.")