# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 14:02:01 2019

@author: Gunardi Saputra
"""

message = "I like you. I miss you. You are my Python now and forever."

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1
    
print(count)
