# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 08:11:35 2019

@author: Gunardi Saputra
"""

stuff = {"rope": 1,
         "torch": 6,
         "gold coin": 66,
         "dagger": 1,
         "arrow": 12,
         "bitcoin": 666}

def displayInventory(inventory):
    print("Inventory: ")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total += v
        print("Total number of items: " + str(item_total))
        
displayInventory(stuff)

