# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 23:36:38 2019

@author: Gunardi Saputra
"""


import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return "It is " + str(answerNumber) 
    elif answerNumber == 2:
        return "It is " + str(answerNumber)
    elif answerNumber == 3:
        return "It is " + str(answerNumber)
    elif answerNumber == 4:
        return "It is " + str(answerNumber)
    elif answerNumber == 5:
        return "It is " + str(answerNumber)
    elif answerNumber == 6:
        return "It is " + str(answerNumber)
    elif answerNumber == 7:
        return "It is " + str(answerNumber)
    elif answerNumber == 8:
        return "It is " + str(answerNumber)
    elif answerNumber == 9:
        return "It is " + str(answerNumber)
    
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)