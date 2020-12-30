# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:45:30 2019

@author: Gunardi Saputra
"""

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True
            
#    print("123-666-1234 is a phone number: ")
#    print(isPhoneNumber("123-666-1234"))
#    print("Wei wei is a phone number: ")
#    print(isPhoneNumber("Wei wei"))
    
message = "Call me at 123-666-1234 tomorrow. 123-666-9999 is my office."
for i in rande(len(message)):
    chunk