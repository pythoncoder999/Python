# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 01:14:24 2019

@author: Gunardi Saputra

Adding magic8Ball2.py
"""
import random

messages = ["It is certain",
            "It is decidedly so",
            "Yes!",
            "Try again!",
            "Ask again later!",
            "Concentrate and ask again!",
            "Outlook not so good",
            "Very doubtful"]



print(messages[random.randint(0, len(messages) - 1)])
