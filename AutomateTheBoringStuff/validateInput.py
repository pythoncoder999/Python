# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 09:02:11 2019

@author: Gunardi Saputra
"""

while True:
    print("Enter your age: ")
    age = input()
    if age.isdecimal():
        break
    print("Please enter a number for your age.")
    
while True:
    print("Select a new password (letters or numbers only):")
    password = input()
    if password.isalnum():
        break
    print("Passwords can only have letters or numbers.")
    