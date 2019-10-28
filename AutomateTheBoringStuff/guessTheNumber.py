# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 00:19:27 2019

@author: Gunardi Saputra
"""
# This is a guess the number game

import random

secretNumber = random.randint(1,16)
print("I am thinking of a number between 1 and 16.")

# Ask the player to guess 6 times/

for guessesTaken in range (1, 7):
    print("Take a guess.")
    guess = int(input())
    
    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        
        print("You are right. The number is " + str(secretNumber))
        break
