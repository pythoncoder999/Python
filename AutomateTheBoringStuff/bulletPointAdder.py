# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 13:36:21 2019

@author: Gunardi Saputra
"""

#! python3
# bulletPointAdder.py = Adds Wikipedia bullet points to the start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()
pyperclip.copy(text)

# Separate lines and add stars.
lines = text.split("\n")
for i in range(len(lines)): # loop throug all indexes in the "lines" list
    lines[i] = "* " + lines[i] # add star to each string in "lines" list
text = "\n".join(lines)
pyperclip.copy(text)

