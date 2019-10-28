# -*- coding: utf-8 -*-
"""
Spyder Editor

author: Gunardi Saputra
"""

def printPicnic(itemsDict, leftWidth, rightWidth):
    print("PICNIC ITEMS".center(leftWidth + rightWidth, "+"))
    for l, r in itemsDict.items():
        print(l.ljust(leftWidth, ".") + str(r).rjust(rightWidth))
picnicItems = {
                "sandwiches": 6,
                "apples": 12,
                "cups": 6,
                "cookies": 666
                }
printPicnic(picnicItems, 15, 5)
printPicnic(picnicItems, 20, 6)


